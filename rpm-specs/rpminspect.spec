Name:           rpminspect
Version:        0.13
Release:        1%{?dist}
Summary:        Build deviation compliance tool
Group:          Development/Tools
License:        GPLv3+
URL:            https://github.com/rpminspect/rpminspect
Source0:        https://github.com/rpminspect/rpminspect/releases/download/v0.13/rpminspect-0.13.tar.xz
Source1:        changelog

Requires:       librpminspect%{?_isa} = %{version}-%{release}

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  json-c-devel
BuildRequires:  xmlrpc-c-devel >= 1.32.5
BuildRequires:  libxml2-devel
BuildRequires:  rpm-devel
BuildRequires:  libarchive-devel
BuildRequires:  elfutils-devel
BuildRequires:  kmod-devel
BuildRequires:  libcurl-devel
BuildRequires:  zlib-devel
BuildRequires:  libmandoc-devel
BuildRequires:  iniparser-devel >= 3.1
BuildRequires:  libyaml-devel
BuildRequires:  file-devel
BuildRequires:  openssl-devel
BuildRequires:  libcap-devel
BuildRequires:  gettext-devel

# The test suite requires additional packages, but they are not used
# in the package building systems.  They are noted here for reference
# by the Makefile and other developers.
#BuildRequires: glibc.i686
#BuildRequires: glibc-devel.i686
#BuildRequires: CUnit
#BuildRequires: CUnit-devel
#BuildRequires: kernel-devel
#BuildRequires: libgcc.i686

%description
Build deviation and compliance tool.  This program runs a number of tests
against one or two builds of source RPM files.  The built artifacts are
inspected and compared to report changes and validate policy compliance
against the defined parameters.


%package -n librpminspect
Summary:        Library providing RPM test API and functionality
Group:          Development/Tools
Requires:       rpminspect-data
Requires:       desktop-file-utils
Requires:       gzip
Requires:       bzip2
Requires:       xz
Requires:       elfutils
Requires:       gettext
Requires:       diffutils

# These are required for libxml2 DTD validation
Requires:       xhtml1-dtds
Requires:       html401-dtds

# These programs are only required for the 'shellsyntax' functionality.
# You can use rpminspect without these installed, just disable the
# shellsyntax inspection.
%if 0%{?rhel} >= 8 || 0%{?epel} >= 8 || 0%{?fedora}
Suggests:       dash
Suggests:       ksh
Suggests:       zsh
Suggests:       tcsh
Suggests:       rc
Suggests:       bash
%else
Requires:       dash
Requires:       ksh
Requires:       zsh
Requires:       tcsh
Requires:       rc
Requires:       bash
%endif

# The annocheck program is used by the annocheck inspection.  It is not
# required.
%if 0%{?rhel} >= 8 || 0%{?epel} >= 8 || 0%{?fedora}
Suggests:       /usr/bin/annocheck
%else
Requires:       /usr/bin/annocheck
%endif

%description -n librpminspect
The library providing the backend test functionality and API for the
rpminspect frontend program.  This library can also be used by other
programs wanting to incorporate RPM test functionality.


%package -n librpminspect-devel
Summary:         Header files and development libraries for librpminspect
Group:           Development/Tools
Requires:        librpminspect%{?_isa} = %{version}-%{release}
Requires:        rpminspect-data

%description -n librpminspect-devel
The header files and development library links required to build software
using librpminspect.


%package -n rpminspect-data-generic
Summary:         Template data files used to drive rpminspect tests
Group:           Development/Tools
Provides:        rpminspect-data

%description -n rpminspect-data-generic
The rpminspect-data-generic package is meant as a template to build your
product's own data file.  The files in it contain product-specific
information.  The files in this package explain how to construct the
control files.


%prep
%setup -q -n rpminspect-0.13


%build
%meson
%meson_build


%install
%meson_install


%files
%doc AUTHORS README TODO
%license COPYING
%{_bindir}/rpminspect
%{_mandir}/man1/rpminspect.1*


%files -n librpminspect
%license COPYING
%{_libdir}/librpminspect.so.*


%files -n librpminspect-devel
%{_includedir}/librpminspect
%{_libdir}/librpminspect.so


%files -n rpminspect-data-generic
%license COPYING
%{_datadir}/rpminspect
%dir %{_sysconfdir}/rpminspect
%config(noreplace) %{_sysconfdir}/rpminspect/rpminspect.conf


%changelog
%include %{SOURCE1}
