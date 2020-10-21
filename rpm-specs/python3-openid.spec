Name:           python3-openid
Version:        3.1.0
Release:        10%{?dist}
Summary:        Python 3 port of the python-openid library
License:        ASL 2.0
URL:            https://github.com/necaris/python3-openid
Source0:        %{pypi_source}

# Python 3.9 compatibility
Patch1:         %{url}/pull/45.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-psycopg2
BuildRequires:  python3-setuptools
BuildRequires:  python3-defusedxml

Requires:       python3-defusedxml

%description
This started out as a fork of the Python OpenID library,
with changes to make it Python 3 compatible.
It's now a port of that library,
including cleanups and updates to the code in general.


%prep
%autosetup -p1

# replace env python shebangs with python3
grep -Erl '^#!/usr/bin/env python$' | xargs \
sed -i -r '1 s|^#!/usr/bin/env python$|#!%{__python3}|g'


%build
%py3_build


%install
%py3_install

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f


%check
%{python3} -m unittest openid.test.test_suite


%files
%doc LICENSE NEWS.md
%dir %{python3_sitelib}/openid
%{python3_sitelib}/openid/*.py
%dir %{python3_sitelib}/openid/__pycache__
%{python3_sitelib}/openid/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/consumer
%{python3_sitelib}/openid/consumer/*.py
%dir %{python3_sitelib}/openid/consumer/__pycache__
%{python3_sitelib}/openid/consumer/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/extensions
%{python3_sitelib}/openid/extensions/*.py
%dir %{python3_sitelib}/openid/extensions/__pycache__
%{python3_sitelib}/openid/extensions/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/extensions/draft
%{python3_sitelib}/openid/extensions/draft/*.py
%dir %{python3_sitelib}/openid/extensions/draft/__pycache__
%{python3_sitelib}/openid/extensions/draft/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/server
%{python3_sitelib}/openid/server/*.py
%dir %{python3_sitelib}/openid/server/__pycache__
%{python3_sitelib}/openid/server/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/store
%{python3_sitelib}/openid/store/*.py
%dir %{python3_sitelib}/openid/store/__pycache__
%{python3_sitelib}/openid/store/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/yadis
%{python3_sitelib}/openid/yadis/*.py
%dir %{python3_sitelib}/openid/yadis/__pycache__
%{python3_sitelib}/openid/yadis/__pycache__/*.pyc
%{python3_sitelib}/python3_openid-%{version}-py3.*.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0, fix FTBFS (#1556287)
- Use nonenv shebangs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Jakub Dorňák <jakub.dornak@misli.cz> - 3.0.10-1
- Update to version 3.0.10

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.9-2
- Require python3-defusedxml

* Thu Nov 19 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.9-1
- Update to version 3.0.9

* Fri Nov 13 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.6-1
- Update to version 3.0.6

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.5-1
- Update to version 3.0.5

* Wed Jun 17 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.2-4
- use BytesIO to write the response (instead of StringIO)
    Resolves: 1232809

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Nov 29 2013 Jakub Dorňák <jdornak@redhat.com> - 3.0.2-1
- Initial package
