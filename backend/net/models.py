from backend.core.extensions import db

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text)
    parent_id = db.Column(db.Integer, db.ForeignKey('notes.id'))
    is_folder = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # __table_args__ = (
    #     db.Index('idx_parent', 'parent_id'),  # 加速文件夹查询
    #     db.Index('idx_updated', 'updated_at')  # 加速最近修改查询
    # )

class YUXINTestUser(db.Model):
    __bind_key__ = 'yuxin'
    __tablename__ = 'yuxin_user'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class PgyerConfig(db.Model):
    __bind_key__ = 'config'
    __tablename__ = 'pgyer_config'
    __table_args__ = (
        db.UniqueConstraint('apikey', 'appkey', name='uix_apiKey_appKey'),  # 名称+API Key组合唯一
    )
    config_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True) #描述名称
    apikey = db.Column(db.String(80), nullable=False)
    appkey = db.Column(db.String(80), nullable=False)
