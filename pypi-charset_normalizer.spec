#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-charset_normalizer
Version  : 2.1.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/93/1d/d9392056df6670ae2a29fcb04cfa5cee9f6fbde7311a1bb511d4115e9b7a/charset-normalizer-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/1d/d9392056df6670ae2a29fcb04cfa5cee9f6fbde7311a1bb511d4115e9b7a/charset-normalizer-2.1.0.tar.gz
Summary  : The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
Group    : Development/Tools
License  : MIT
Requires: pypi-charset_normalizer-bin = %{version}-%{release}
Requires: pypi-charset_normalizer-license = %{version}-%{release}
Requires: pypi-charset_normalizer-python = %{version}-%{release}
Requires: pypi-charset_normalizer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
<h1 align="center">Charset Detection, for Everyone 👋 <a href="https://twitter.com/intent/tweet?text=The%20Real%20First%20Universal%20Charset%20%26%20Language%20Detector&url=https://www.github.com/Ousret/charset_normalizer&hashtags=python,encoding,chardet,developers"><img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"/></a></h1>

%package bin
Summary: bin components for the pypi-charset_normalizer package.
Group: Binaries
Requires: pypi-charset_normalizer-license = %{version}-%{release}

%description bin
bin components for the pypi-charset_normalizer package.


%package license
Summary: license components for the pypi-charset_normalizer package.
Group: Default

%description license
license components for the pypi-charset_normalizer package.


%package python
Summary: python components for the pypi-charset_normalizer package.
Group: Default
Requires: pypi-charset_normalizer-python3 = %{version}-%{release}

%description python
python components for the pypi-charset_normalizer package.


%package python3
Summary: python3 components for the pypi-charset_normalizer package.
Group: Default
Requires: python3-core
Provides: pypi(charset_normalizer)

%description python3
python3 components for the pypi-charset_normalizer package.


%prep
%setup -q -n charset-normalizer-2.1.0
cd %{_builddir}/charset-normalizer-2.1.0
pushd ..
cp -a charset-normalizer-2.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656364651
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-charset_normalizer
cp %{_builddir}/charset-normalizer-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-charset_normalizer/753eb879a99db2b65e384b3c1baec552b6134f26
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/normalizer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-charset_normalizer/753eb879a99db2b65e384b3c1baec552b6134f26

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
