%global srcname social-auth-core
%global desc Python Social Auth is an easy to setup social \
authentication/registration mechanism with support for several frameworks and \
auth providers. This is the core component of the python-social-auth ecosystem, \
it implements the common interface to define new authentication backends to \
third parties services, implement integrations with web frameworks and storage \
solutions. \

Name:           python-%{srcname}
Version:        1.7.0
Release:        11%{?dist}
Summary:        The core component of the python-social-auth ecosystem

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/python-social-auth/social-core/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         Unpin-the-test-requirements-and-use-unittest2-for-Py.patch

BuildArch:      noarch
BuildRequires:  python3-devel


%description
%{desc}


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: %{py3_dist cryptography}
BuildRequires: %{py3_dist nose}
BuildRequires: %{py3_dist httpretty}
BuildRequires: %{py3_dist defusedxml}
BuildRequires: %{py3_dist python3-openid}
BuildRequires: %{py3_dist python3-saml}
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist oauthlib}
BuildRequires: %{py3_dist requests-oauthlib}
BuildRequires: %{py3_dist six}
BuildRequires: %{py3_dist PyJWT}
Requires: %{py3_dist cryptography}
Requires: %{py3_dist defusedxml}
Requires: %{py3_dist python3-openid}
Requires: %{py3_dist python3-saml}
Requires: %{py3_dist requests}
Requires: %{py3_dist oauthlib}
Requires: %{py3_dist requests-oauthlib}
Requires: %{py3_dist six}
Requires: %{py3_dist PyJWT}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n social-core-%{version}
rm -f requirements-openidconnect.txt
touch requirements-openidconnect.txt
rm -f social_core/tests/requirements-base.txt
touch social_core/tests/requirements-base.txt

sed -i -e 's|defusedxml>=0.5.0rc1|defusedxml>=0.5.0|' requirements-python3.txt

sed -i /unittest2/d social_core/tests/requirements-python3.txt
sed -i s/unittest2/unittest/ social_core/tests/*.py social_core/tests/*/*.py

%build
%py3_build


%install
%py3_install


%check
%__python3 setup.py test


%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.0-9
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-5
- Change the defusedxml requirement to not have rc1, which confused the python auto dep script.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.7.0-1
- Initial package.
