from bclib.blockchain import CBlock, SampleClass


def test_root_cblock():
    root = CBlock('I am root', None)
    assert root is not None


def test_root_children():
    root = CBlock(b'I am root', None)
    b1 = CBlock(b'I am a child', root)
    b2 = CBlock(b"I am B1's brother", root)
    b3 = CBlock(12345, root)
    assert b1 is not None
    assert b2 is not None
    assert b3 is not None


def test_root_grandchild():
    root = CBlock('I am root', None)
    b2 = CBlock("I am B1's brother", root)
    b4 = CBlock(SampleClass('Hi there!'), b2)
    assert b4 is not None


def test_hashing():
    root = CBlock('I am root', None)
    b1 = CBlock('I am a child', root)
    b2 = CBlock("I am B1's brother", root)
    b3 = CBlock(12345, root)
    b4 = CBlock(SampleClass('Hi there!'), b2)
    b5 = CBlock('Top block', b4)

    for b in [b1, b2, b3, b4, b5]:
        assert b.previousBlock.computeHash() == b.previousHash
