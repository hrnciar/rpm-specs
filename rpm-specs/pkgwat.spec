%global modname pkgwat.cli

Name:             pkgwat
Version:          0.13
Release:          6%{?dist}
Summary:          CLI tool for querying the fedora packages webapp

License:          LGPLv2+
URL:              https://pypi.python.org/pypi/pkgwat.cli
Source0:          https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools

%global _description\
Pronounced "package WAT", pkgwat is a fast CLI tool for querying the fedora\
packages webapp.  https://apps.fedoraproject.org/packages/\
\
You can make its search even better by helping us tag packages.\
https://apps.fedoraproject.org/tagger

%description %_description

%package -n python3-pkgwat
Summary:          Python API for querying the fedora packages webapp

Requires:         python3-pkgwat-api
Requires:         python3-cliff

%description -n python3-pkgwat
Pronounced "package WAT", pkgwat is a fast CLI tool for querying the fedora
packages webapp.  https://apps.fedoraproject.org/packages/

You can make its search even better by helping us tag packages.
https://apps.fedoraproject.org/tagger

%prep
%setup -q -n %{modname}-%{version}
sed -i "s/»/>/g" README.rst
sed -i '/pillow/d' setup.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}

%files -n python3-pkgwat
%doc LICENSE README.rst
%{python3_sitelib}/pkgwat/cli
%{python3_sitelib}/%{modname}-%{version}-*
%{_bindir}/pkgwat

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Kamil Páral <kparal@redhat.com> - 0.13-1
- Release 0.13

* Sun Feb 03 2019 Kevin Fenzi <kevin@scrye.com> - 0.11-14
- Drop python2 subpackages. Fixes bug #1472362

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11-11
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11-8
- Python 2 binary package renamed to python2-pkgwat
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Mon Jul 31 2017 Kevin Fenzi <kevin@scrye.com> - 0.11-7
- Enable python3 now. Fixes bug #1472362

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Ralph Bean <rbean@redhat.com> - 0.11-1
- Latest upstream.

* Wed Oct 01 2014 Ralph Bean <rbean@redhat.com> - 0.10-3
- Define python2 macros for el6.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Ralph Bean <rbean@redhat.com> - 0.10-1
- Added short flags for pagination.

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.9-1
- Latest upstream with bugfixes for link shortening.
- Modernize python2 rpm macros.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Ralph Bean <rbean@redhat.com> - 0.8-1
- New pkgwat history subcommand.
- Fix to pkgwat search.

* Thu Jun 13 2013 Ralph Bean <rbean@redhat.com> - 0.7-1
- Latest upstream with datagrepper query.
- Fix when getting info on a subpackage from Ariel Barria.

* Tue May 14 2013 Ralph Bean <rbean@redhat.com> - 0.6-2
- Adjust sed statement.

* Tue May 14 2013 Ralph Bean <rbean@redhat.com> - 0.6-1
- Latest upstream.  Fixes issue with PIL/Pillow.
- Removed downstream patch.

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 0.5-2
- Patch to fix a bug in the updates subcommand.

* Tue Jan 22 2013 Ralph Bean <rbean@redhat.com> - 0.5-1
- Latest upstream.
- Fix a unicode bug when redirecting to files.
- Properly display multi-build updates.

* Wed Jan 16 2013 Ralph Bean <rbean@redhat.com> - 0.4-2
- Remove no-longer-necessary Requires on python-imaging.
- Patch PIL requirement out of setup.py.

* Thu Nov 08 2012 Ralph Bean <rbean@redhat.com> - 0.4-1
- Fixed bug with latest python-requests.
- Gracefully handle unknown commands.

* Fri Nov 02 2012 Ralph Bean <rbean@redhat.com> - 0.3-3
- Bugfix - Require python-imaging and python-fabulous.

* Thu Jul 05 2012 Ralph Bean <rbean@redhat.com> - 0.3-2
- Manually disable python3 support until python3-cliff is available.

* Mon Jul 02 2012 Ralph Bean <rbean@redhat.com> - 0.3-1
- Initial package for Fedora
