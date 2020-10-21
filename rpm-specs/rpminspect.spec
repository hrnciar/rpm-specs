Name:           rpminspect
Version:        1.1
Release:        1%{?dist}
Summary:        Build deviation compliance tool
Group:          Development/Tools
# librpminspect is licensed under the LGPLv3+, but 5 source files in
# the library are from an Apache 2.0 licensed project.  The
# rpminspect(1) command line tool is licensed under the GPLv3+.  And
# the rpminspect-data-generic package is licensed under the CC-BY-4.0
# license.
License:        GPLv3+ and LGPLv2+ and ASL 2.0 and CC-BY
URL:            https://github.com/rpminspect/rpminspect
Source0:        https://github.com/rpminspect/rpminspect/releases/download/v1.1/rpminspect-1.1.tar.xz
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
BuildRequires:  libyaml-devel
BuildRequires:  file-devel
BuildRequires:  openssl-devel
BuildRequires:  libcap-devel
BuildRequires:  gettext-devel

# This block can be removed when all targeted platforms have 1.14.5.
# The 1.14.5 mandoc package has libmandoc.a and fixes for some known
# problems, which we want for librpminspect.  Fedora <= 30 and EPEL <=
# 7 do not currently have this build.  When they do, reduce this block
# to a single BuildRequires line.
%if 0%{?rhel} >= 8 || 0%{?epel} >= 8 || 0%{?fedora} >= 31
BuildRequires:  libmandoc-devel >= 1.14.5
%else
BuildRequires:  libmandoc-devel
%endif

%description
Build deviation and compliance tool.  This program runs a number of tests
against one or two builds of source RPM files.  The built artifacts are
inspected and compared to report changes and validate policy compliance
against the defined parameters.


%package -n librpminspect
Summary:        Library providing RPM test API and functionality
Group:          Development/Tools
Requires:       desktop-file-utils
Requires:       gzip
Requires:       bzip2
Requires:       xz
Requires:       gettext
Requires:       diffutils

# If these are present, the xml inspection can try DTD validation.
%if 0%{?rhel} >= 8 || 0%{?fedora}
Suggests:       xhtml1-dtds
Suggests:       html401-dtds
%endif

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

# The annocheck program is used by the annocheck inspection.  If it is
# not present, you can disable the annocheck inspection.
%if 0%{?rhel} >= 8 || 0%{?epel} >= 8 || 0%{?fedora}
Suggests:       /usr/bin/annocheck
%else
Requires:       /usr/bin/annocheck
%endif

# The abidiff program is used by the abidiff inspection.  If it is not
# present, you can disable the abidiff inspection.
%if 0%{?rhel} >= 8 || 0%{?epel} >= 8 || 0%{?fedora}
Suggests:       /usr/bin/abidiff
%else
Requires:       /usr/bin/abidiff
%endif

# The kmidiff program is used by the kmidiff inspection.  If it is not
# present, you can disable the kmidiff inspection.
%if 0%{?rhel} >= 8 || 0%{?epel} >= 8 || 0%{?fedora}
Suggests:       /usr/bin/kmidiff
%else
Requires:       /usr/bin/kmidiff
%endif

%description -n librpminspect
The library providing the backend test functionality and API for the
rpminspect frontend program.  This library can also be used by other
programs wanting to incorporate RPM test functionality.


%package -n librpminspect-devel
Summary:         Header files and development libraries for librpminspect
Group:           Development/Tools
Requires:        librpminspect%{?_isa} = %{version}-%{release}

%description -n librpminspect-devel
The header files and development library links required to build software
using librpminspect.


%package -n rpminspect-data-generic
Summary:         Template data files used to drive rpminspect tests
Group:           Development/Tools

%description -n rpminspect-data-generic
The rpminspect-data-generic package is meant as a template to build your
product's own data file.  The files in it contain product-specific
information.  The files in this package explain how to construct the
control files.


%prep
%setup -q -n rpminspect-1.1


%build
%meson -Dtests=false
%meson_build


%install
%meson_install


%files
%doc AUTHORS.md README.md TODO
%license COPYING
%{_bindir}/rpminspect
%{_mandir}/man1/rpminspect.1*


%files -n librpminspect
%license COPYING.LIB LICENSE-2.0.txt
%{_libdir}/librpminspect.so.*


%files -n librpminspect-devel
%license COPYING.LIB
%{_includedir}/librpminspect
%{_libdir}/librpminspect.so


%files -n rpminspect-data-generic
%license CC-BY-4.0.txt
%{_datadir}/rpminspect


%changelog
%include %{SOURCE1}
