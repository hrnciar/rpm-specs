%global module_name bmaptools

Name:           bmap-tools
Version:        3.5
Release:        4%{?dist}
Summary:        Tools to generate and flash sparse images using the "block map" (bmap) format
License:        GPLv2+
URL:            https://github.com/intel/bmap-tools
Source0:        https://github.com/intel/bmap-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/intel/bmap-tools/commit/db7087b883bf52cbff063ad17a41cc1cbb85104
# Fixes https://github.com/intel/bmap-tools/issues/57 for Python 3.7+
Patch1:         db7087b883bf52cbff063ad17a41cc1cbb85104d.patch
BuildArch:      noarch
# Base package contains the command line tool, which uses the Python library
Requires:       python3-%{module_name} = %{version}-%{release}

%description
Tools to generate "block map" (a.k.a. bmap) files and flash images. Bmaptool is
a generic tool for creating the block map (bmap) for a file, and copying files
using the block map. The idea is that large file containing unused blocks, like
raw system image files, can be copied or flashed a lot faster with bmaptool
than with traditional tools like "dd" or "cp". See
https://source.tizen.org/documentation/reference/bmaptool for more information.

%package -n python3-%{module_name}
Summary:        Python library to manipulate sparse images in the "block map" (bmap) format
%{?python_provide:%python_provide python3-%{module_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-six
Requires:       python3-six
Requires:       python3-gpg
Requires:       bzip2
Requires:       pbzip2
Requires:       gzip
Requires:       xz
Requires:       tar
Requires:       unzip
Requires:       lzop
Requires:       pigz

%description -n python3-%{module_name}
Python library for bmap-tools.

%prep
%setup -q
%patch1 -p1
# Remove unnecessary shebang
sed -i -e '/^#!/,1d' bmaptools/CLI.py

%build
%py3_build

%install
%py3_install
install -d %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1

%check
nosetests-3

%files
%{_bindir}/bmaptool
%{_mandir}/man1/bmaptool.1*

%files -n python3-%{module_name}
%doc docs/README docs/RELEASE_NOTES
%license COPYING
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/bmap_tools*.egg-info

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5-3
- Rebuilt for Python 3.9

* Mon Dec 30 2019 Dan Callaghan <dan.callaghan@opengear.com> - 3.5-2
- dropped the separate 'bmaptool' subpackage, the base package now provides
  /usr/bin/bmaptool

* Tue Jan 29 2019 Dan Callaghan <dan.callaghan@opengear.com> - 3.5-1
- initial version
