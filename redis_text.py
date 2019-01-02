from redis import StrictRedis


# 创建redis链接对象
if __name__ == '__main__':
    try:
        sr = StrictRedis(host="127.0.0.1",
                         port=6379,
                         db=12,
                         decode_responses=True
                         )
        # sr.mset(a="python", b="java", c="php")
        sr.mset({"a":"python", "b":"java", "c":"c++"})
        # sr.set("a", "python")
        # sr.set("b", "java")
        print(sr.mget("a", "b", "c"))

        sr.delete("b", "c")
        print(sr.keys())

        sr.hmset("user", {"name":"python", "age":"28"})
        print(sr.hkeys("user"))
        print(sr.hmget("user", "name", "age"))

    except Exception as e:
        print(e)

    else:
        pass
