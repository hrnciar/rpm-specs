%global modname vcrpy

Name:               python-vcrpy
Version:            4.0.2
Release:            2%{?dist}
Summary:            Automatically mock your HTTP interactions to simplify and speed up testing

License:            MIT
URL:                https://pypi.io/project/vcrpy
Source0:            %pypi_source %{modname}

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

BuildRequires:      python3-PyYAML
BuildRequires:      python3-mock
BuildRequires:      python3-six
BuildRequires:      python3-contextlib2
BuildRequires:      python3-wrapt
#BuildRequires:      python3-backport_collections

BuildRequires:      python3-pytest
BuildRequires:      python3-yarl
BuildRequires:      python3-pytest-mock
BuildRequires:      python3-pytest-httpbin
BuildRequires:      python3-aiohttp
BuildRequires:      python3-botocore
BuildRequires:      python3-boto3
BuildRequires:      python3-boto
BuildRequires:      python3-requests
BuildRequires:      python3-urllib3
BuildRequires:      python3-tornado
BuildRequires:      python3-httplib2

%global _description\
Simplify and speed up testing HTTP by recording all HTTP interactions and\
saving them to "cassette" files, which are yaml files containing the contents\
of your requests and responses.  Then when you run your tests again, they all\
just hit the text files instead of the internet.  This speeds up your tests and\
lets you work offline.\
\
If the server you are testing against ever changes its API, all you need to do\
is delete your existing cassette files, and run your tests again.  All of the\
mocked responses will be updated with the new API.

%description %_description

%package -n python3-vcrpy
Summary:            Automatically mock your HTTP interactions to simplify and speed up testing

Requires:           python3-PyYAML
Requires:           python3-mock
Requires:           python3-six
Requires:           python3-contextlib2
Requires:           python3-wrapt
#Requires:           python3-backport_collections
%{?python_provide:%python_provide python3-vcrpy}


%description -n python3-vcrpy
Simplify and speed up testing HTTP by recording all HTTP interactions and
saving them to "cassette" files, which are yaml files containing the contents
of your requests and responses.  Then when you run your tests again, they all
just hit the text files instead of the internet.  This speeds up your tests and
lets you work offline.

If the server you are testing against ever changes its API, all you need to do
is delete your existing cassette files, and run your tests again.  All of the
mocked responses will be updated with the new API.

%prep
%setup -q -n %{modname}-%{version}

sed -i "s/backport_collections/collections/g" vcr/filters.py
sed -i "s/backport_collections/collections/g" vcr/cassette.py
sed -i "s/, 'backport_collections'//g" setup.py

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-vcrpy
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/vcr/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.2-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Clément Verna <cverna@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2 Fixes bug 1768194

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Kevin Fenzi <kevin@scrye.com> - 2.1.0-1
- Update to 2.1.0. Fixes bug 1742605
- Enabled all tests in check.

* Wed Sep 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-5
- Subpackage python2-vcrpy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.13.0
- Update to 1.13.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-4
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Kevin Fenzi <kevin@scrye.com> - 1.11.1-1
- Update to 1.11.1. Fixes bug #1447325

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.10.5-4
- Python 2 binary package renamed to python2-vcrpy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Kevin Fenzi <kevin@scrye.com> - 1.10.5-1
- Update to 1.10.5. Fixes bug #1412604

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.10.4-2
- Rebuild for Python 3.6

* Fri Dec 16 2016 Ralph Bean <rbean@redhat.com> - 1.10.4-1
- new version

* Sun Oct 02 2016 Kevin Fenzi <kevin@scrye.com> - 1.10.3-1
- Update to 1.10.3. Fixes bug #1381102

* Sat Sep 17 2016 Kevin Fenzi <kevin@scrye.com> - 1.10.2-1
- Update to 1.10.2. Fixes bug #1376311

* Mon Sep 12 2016 Kevin Fenzi <kevin@scrye.com> - 1.10.1-1
- Update to 1.10.1.

* Fri Sep 09 2016 Kevin Fenzi <kevin@scrye.com> - 1.10.0-1
- Update to 1.10.0. Fixes bug #1370830

* Wed Jul 27 2016 Ralph Bean <rbean@redhat.com> - 1.9.0-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Ralph Bean <rbean@redhat.com> - 1.8.0-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Ralph Bean <rbean@redhat.com> - 1.7.4-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 1.7.3-1
- new version

* Mon Jul 06 2015 Ralph Bean <rbean@redhat.com> - 1.6.0-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Ralph Bean <rbean@redhat.com> - 1.5.2-2
- Move python3 deps into the python3 subpackage.

* Sat May 16 2015 Ralph Bean <rbean@redhat.com> - 1.5.2-1
- new version

* Fri May 15 2015 Ralph Bean <rbean@redhat.com> - 1.5.1-1
- new version

* Wed May 06 2015 Ralph Bean <rbean@redhat.com> - 1.4.2-1
- Adjusted spec with feedback from package review.
- Fix original changelog entry.
- Fix directory ownership in the files section.
- Latest upstream.

* Sat Apr 11 2015 Ralph Bean <rbean@redhat.com> 1.4.0-1
- initial package for Fedora
