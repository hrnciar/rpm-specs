Name:           python3-saml
Version:        1.9.0
Release:        3%{?dist}
Summary:        Add SAML support to your Python software using this library

License:        MIT
URL:            https://pypi.python.org/pypi/%{name}
Source0:        https://github.com/onelogin/python3-saml/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires: %{py3_dist freezegun isodate xmlsec defusedxml}
Requires: %{py3_dist isodate xmlsec defusedxml}


%description
This toolkit lets you turn your Python application into a SP
(Service Provider) that can be connected to an IdP (Identity Provider).


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%check
%__python3 setup.py test


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-2
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Ken Dreyer <kdreyer@redhat.com> - 1.9.0-1
- Update to 1.9.0 (rhbz#1726650)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0.
- Relax defusedxml requirement. Fixes bug #1723432

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.0-1
- Initial package.
