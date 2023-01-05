#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_client
Version  : 7.4.8
Release  : 98
URL      : https://files.pythonhosted.org/packages/76/e5/5213bf5edc3250c5c19135e3f04e3bc6573d2f694fab07ac9f6d75a582cf/jupyter_client-7.4.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/76/e5/5213bf5edc3250c5c19135e3f04e3bc6573d2f694fab07ac9f6d75a582cf/jupyter_client-7.4.8.tar.gz
Summary  : Jupyter protocol implementation and client libraries
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_client-bin = %{version}-%{release}
Requires: pypi-jupyter_client-license = %{version}-%{release}
Requires: pypi-jupyter_client-python = %{version}-%{release}
Requires: pypi-jupyter_client-python3 = %{version}-%{release}
Requires: pypi(pyzmq)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Jupyter Client
[![Build Status](https://github.com/jupyter/jupyter_client/workflows/CI/badge.svg)](https://github.com/jupyter/jupyter_client/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

%package bin
Summary: bin components for the pypi-jupyter_client package.
Group: Binaries
Requires: pypi-jupyter_client-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_client package.


%package license
Summary: license components for the pypi-jupyter_client package.
Group: Default

%description license
license components for the pypi-jupyter_client package.


%package python
Summary: python components for the pypi-jupyter_client package.
Group: Default
Requires: pypi-jupyter_client-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_client package.


%package python3
Summary: python3 components for the pypi-jupyter_client package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_client)
Requires: pypi(entrypoints)
Requires: pypi(jupyter_core)
Requires: pypi(nest_asyncio)
Requires: pypi(python_dateutil)
Requires: pypi(pyzmq)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-jupyter_client package.


%prep
%setup -q -n jupyter_client-7.4.8
cd %{_builddir}/jupyter_client-7.4.8
pushd ..
cp -a jupyter_client-7.4.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672285308
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_client
cp %{_builddir}/jupyter_client-%{version}/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-jupyter_client/8fd549f28c3423c251b3b70e91bdad2fbfe6ef30 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-kernel
/usr/bin/jupyter-kernelspec
/usr/bin/jupyter-run

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_client/8fd549f28c3423c251b3b70e91bdad2fbfe6ef30

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
