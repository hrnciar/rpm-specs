%global forgeurl    https://github.com/alzeih/pass-pwned
Version:            0.1.1

%forgemeta

Name:           pass-pwned
Release:        3%{?dist}
Summary:        Password-Store extension for Have I Been Pwned

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  make
Requires:       pass
Requires:       curl

%description
Password-Store extension for Have I Been Pwned? Pwned Passwords v2 API.

In order to protect the value of the source password being searched for,
Pwned Passwords also implements a k-Anonymity model that allows a password
to be searched for by partial hash. This allows the first 5 characters of a
SHA-1 password hash (not case-sensitive) to be passed to the API.

%prep
%forgesetup
%autosetup

%build

%install
%make_install

%files
%license LICENSE
%doc README.md
%doc %{_mandir}/man1/pass-pwned.1*
%{_usr}/lib/password-store/extensions/pwned.bash
%{_sysconfdir}/bash_completion.d/pass-pwned

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Brian (bex) Exelbierd <bex@pobox.com> - 0.1.1-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Brian (bex) Exelbierd <bexelbie@redhat.com> - 0.1.0-1
- Updated for new release - now using actual releases in the upstream
* Tue Jun 04 2019 Brian (bex) Exelbierd <bexelbie@redhat.com> - 0-0.1.20190516gitc4cf64d
- New Version
* Thu May 16 2019 Brian (bex) Exelbierd <bexelbie@redhat.com> - 0-0.1.20190516git884856e
- Initial package
