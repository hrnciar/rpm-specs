Name:           urlscan
Version:        0.9.5
Release:        1%{?dist}
Summary:        Extract and browse the URLs contained in an email (urlview replacement)

License:        GPLv2+
URL:            https://github.com/firecat53/%{name}
Source0:        https://github.com/firecat53/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        muttrc
Patch0:         %{name}-remove-doc.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-urwid >= 1.2.1


%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.


%prep
%autosetup -p1
cp -p %{SOURCE1} .


%build
%py3_build


%install
%py3_install


%files
%license COPYING
%doc muttrc README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/*


%changelog
* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.5-1
- Update to new release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-4
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.4-1
- Update to new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.3-1
- Update to new version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.7-2
- Rebuilt for Python 3.7

* Fri Mar 02 2018 Filip Szymański <fszymanski@fedoraproject.org> - 0.8.7-1
- Update to 0.8.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Filip Szymański <fszymanski@fedoraproject.org> - 0.8.6-2
- Copy muttrc file in %%prep section

* Thu Dec 21 2017 Filip Szymański <fszymanski@fedoraproject.org> - 0.8.6-1
- Initial release
