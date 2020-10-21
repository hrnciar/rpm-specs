Name:           git-secret
Version:        0.3.2
Release:        4%{?dist}
Summary:        A bash-tool to store your private data inside a git repository

License:        MIT
URL:            http://git-secret.io/
Source0:        https://github.com/sobolevn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash        >= 3.2.57
Requires:       gawk        >= 4.0.2
Requires:       git         >= 1.8.3.1
Requires:       gpg         >= 1.4
# sha256sum is needed, provided in coreutils

%description
git-secret is a bash tool which stores private data inside a git repository.
It encrypts tracked files with public keys for users whom you trust using GPG,
allowing permitted users to access encrypted data using their secret keys.

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%license LICENSE.md
%{_bindir}/git-secret
%{_mandir}/man1/git-secret*
%{_mandir}/man7/git-secret*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 22 2019 Gergely Gombos <gombosg@gmail.com> 0.3.2-2
- remove sha256sum dependency as nothing provides it (in coreutils)

* Sun Sep 22 2019 Gergely Gombos <gombosg@gmail.com> 0.3.2-1
- 0.3.2 upgrade, clarify sha256sum dependency
 
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Gergely Gombos <gombosg@gmail.com> 0.2.6-1
- 0.2.6 upgrade

* Mon Mar 4 2019 Gergely Gombos <gombosg@gmail.com> 0.2.5-2
- Fix reviewer comments

* Mon Mar 4 2019 Gergely Gombos <gombosg@gmail.com> 0.2.5-1
- Initial packaging for review submission
