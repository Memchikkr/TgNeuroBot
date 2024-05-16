import replicate

from typing import Any, Dict
from aiogram.types import Message
from config import project_settings


class ReplicateService:

    REPLICATE_API_TOKEN = project_settings.replicate_api_token
    models = {
        'realvisxl': 'lucataco/realvisxl2-lcm:479633443fc6588e1e8ae764b79cdb3702d0c196e0cb2de6db39ce577383be77',
        'rembg': 'cjwbw/rembg:fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003'
    }

    @classmethod
    async def get_answer(cls, data: Dict[str, Any]):
        ref = data.pop('ref')
        ref = cls.models[ref]
        generated_images = await replicate.async_run(ref=ref, input=data)
        if isinstance(generated_images, str):
            image = generated_images
        else:
            image = generated_images[0]
        return image
