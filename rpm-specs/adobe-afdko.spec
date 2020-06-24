%global archivename afdko

Name:		adobe-afdko
Version:	3.3.0
Release:	1%{?dist}
Summary:	Adobe Font Development Kit for OpenType
License:	ASL 2.0
URL:		https://github.com/adobe-type-tools/afdko
Source0:	https://github.com/adobe-type-tools/%{archivename}/releases/download/%{version}/%{archivename}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make

%description
Adobe Font Development Kit for OpenType (AFDKO).
The AFDKO is a set of tools for building OpenType font files
from PostScript and TrueType font data.

%prep
%autosetup -n %{archivename}-%{version}

%build
%set_build_flags
pushd c
sh buildalllinux.sh release
popd

%install
install -m 0755 -d %{buildroot}/%{_bindir}
pushd c/build_all
find ./ -type f -executable -exec install -p -m 0755 "{}" \
	%{buildroot}/%{_bindir} ";"

%files
%license LICENSE.md
%doc docs/ README.md NEWS.md
%{_bindir}/*

%changelog
* Mon May 18 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.3.0-1
- Build for latest release 3.3.0

* Sat May 09 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.2.0-2
- undo the change 'Rename makeotfexe to makeotf'

* Fri Apr 3 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.2.0-1
- Build for latest release

* Mon Mar 23 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-4
- rename package name afdko to adobe-afdko

* Mon Mar 9 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-3
- Added %%set_build_flags
- Updated install script

* Mon Mar 2 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.1-2
- Added build dependency gcc, make
- Removed unused build dependency
- Rename makeotfexe to makeotf

* Fri Dec 13 2019 Peng Wu <pwu@redhat.com> - 3.0.1-1
- Initial Version
