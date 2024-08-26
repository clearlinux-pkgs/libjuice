#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
Name     : libjuice
Version  : 1.5.3
Release  : 4
URL      : https://github.com/paullouisageneau/libjuice/archive/v1.5.3/libjuice-1.5.3.tar.gz
Source0  : https://github.com/paullouisageneau/libjuice/archive/v1.5.3/libjuice-1.5.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libjuice-lib = %{version}-%{release}
Requires: libjuice-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(nettle)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# libjuice - UDP Interactive Connectivity Establishment
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-blue.svg)](https://www.mozilla.org/en-US/MPL/2.0/)
[![Build and test](https://github.com/paullouisageneau/libjuice/actions/workflows/build.yml/badge.svg)](https://github.com/paullouisageneau/libjuice/actions/workflows/build.yml)
[![Packaging status](https://repology.org/badge/tiny-repos/libjuice.svg)](https://repology.org/project/libjuice/versions)
[![Latest packaged version](https://repology.org/badge/latest-versions/libjuice.svg)](https://repology.org/project/libjuice/versions)
[![Gitter](https://badges.gitter.im/libjuice/community.svg)](https://gitter.im/libjuice/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Discord](https://img.shields.io/discord/903257095539925006?logo=discord)](https://discord.gg/jXAP8jp3Nn)

%package dev
Summary: dev components for the libjuice package.
Group: Development
Requires: libjuice-lib = %{version}-%{release}
Provides: libjuice-devel = %{version}-%{release}
Requires: libjuice = %{version}-%{release}

%description dev
dev components for the libjuice package.


%package lib
Summary: lib components for the libjuice package.
Group: Libraries
Requires: libjuice-license = %{version}-%{release}

%description lib
lib components for the libjuice package.


%package license
Summary: license components for the libjuice package.
Group: Default

%description license
license components for the libjuice package.


%prep
%setup -q -n libjuice-1.5.3
cd %{_builddir}/libjuice-1.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724669351
mkdir -p clr-build
pushd clr-build
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
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1724669351
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libjuice
cp %{_builddir}/libjuice-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libjuice/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/juice/juice.h
/usr/lib64/cmake/LibJuice/LibJuiceConfig.cmake
/usr/lib64/cmake/LibJuice/LibJuiceConfigVersion.cmake
/usr/lib64/cmake/LibJuice/LibJuiceTargets-relwithdebinfo.cmake
/usr/lib64/cmake/LibJuice/LibJuiceTargets.cmake
/usr/lib64/libjuice.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjuice.so.1.5.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libjuice/9744cedce099f727b327cd9913a1fdc58a7f5599
