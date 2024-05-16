from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    proxy_login: str
    proxy_password: str
    proxy_url: str
    tg_token: str


project_settings = ProjectSettings()
