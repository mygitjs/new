# 创建和使用虚拟环境
# 虚拟环境是Python中的一个重要概念，它可以帮助我们在同一台机器中同时管理多个项目的依赖，避免不同项目之间的依赖冲突。Python提供了venv模块来创建虚拟环境。
#
# 创建虚拟环境
# 在命令行中输入以下命令来创建一个名为myenv的虚拟环境：
#
# python -m venv myenv

# 激活虚拟环境
# 在Windows系统下，执行以下命令激活虚拟环境：
#
# myenv\Scripts\activate

# 在Mac和Linux系统下，执行以下命令激活虚拟环境：
#
# source myenv/bin/activate

# 退出虚拟环境
# 在虚拟环境中进行开发或使用后，我们可以通过以下命令退出虚拟环境：
#
# deactivate