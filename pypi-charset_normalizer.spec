#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v2
# autospec commit: 250a666
#
Name     : pypi-charset_normalizer
Version  : 3.3.2
Release  : 39
URL      : https://files.pythonhosted.org/packages/63/09/c1bc53dab74b1816a00d8d030de5bf98f724c52c1635e07681d312f20be8/charset-normalizer-3.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/09/c1bc53dab74b1816a00d8d030de5bf98f724c52c1635e07681d312f20be8/charset-normalizer-3.3.2.tar.gz
Summary  : The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
Group    : Development/Tools
License  : MIT
Requires: pypi-charset_normalizer-bin = %{version}-%{release}
Requires: pypi-charset_normalizer-license = %{version}-%{release}
Requires: pypi-charset_normalizer-python = %{version}-%{release}
Requires: pypi-charset_normalizer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<h1 align="center">Charset Detection, for Everyone 👋</h1>
<p align="center">
<sup>The Real First Universal Charset Detector</sup><br>
<a href="https://pypi.org/project/charset-normalizer">
<img src="https://img.shields.io/pypi/pyversions/charset_normalizer.svg?orange=blue" />
</a>
<a href="https://pepy.tech/project/charset-normalizer/">
<img alt="Download Count Total" src="https://static.pepy.tech/badge/charset-normalizer/month" />
</a>
<a href="https://bestpractices.coreinfrastructure.org/projects/7297">
<img src="https://bestpractices.coreinfrastructure.org/projects/7297/badge">
</a>
</p>
<p align="center">
<sup><i>Featured Packages</i></sup><br>
<a href="https://github.com/jawah/niquests">
<img alt="Static Badge" src="https://img.shields.io/badge/Niquests-HTTP_1.1%2C%202%2C_and_3_Client-cyan">
</a>
<a href="https://github.com/jawah/wassima">
<img alt="Static Badge" src="https://img.shields.io/badge/Wassima-Certifi_Killer-cyan">
</a>
</p>
<p align="center">
<sup><i>In other language (unofficial port - by the community)</i></sup><br>
<a href="https://github.com/nickspring/charset-normalizer-rs">
<img alt="Static Badge" src="https://img.shields.io/badge/Rust-red">
</a>
</p>

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
%setup -q -n charset-normalizer-3.3.2
cd %{_builddir}/charset-normalizer-3.3.2
pushd ..
cp -a charset-normalizer-3.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698851377
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-charset_normalizer
cp %{_builddir}/charset-normalizer-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-charset_normalizer/753eb879a99db2b65e384b3c1baec552b6134f26 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
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
