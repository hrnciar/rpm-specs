%global modname jira
%global distname jira
%global eggname jira

Name:               python-%{distname}
Version:            2.0.0
Release:            8%{?dist}
Summary:            A library to ease use of the JIRA 5 REST APIs

License:            BSD
URL:                https://pypi.io/project/%{distname}
Source0:            https://files.pythonhosted.org/packages/source/j/%{distname}/%{distname}-%{version}.tar.gz
Patch0:             python-jira-no-mime-detection.patch

BuildArch:          noarch

BuildRequires:      python3-sphinx

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pbr
BuildRequires:      python3-sphinx
BuildRequires:      python3-pytest-runner

BuildRequires:      python3-pytest-cov

%description
A library to ease use of the JIRA 5 REST APIs.


%package -n python3-%{distname}
Summary:            %{summary}
Requires:           python3-requests
Requires:           python3-requests-oauthlib
Requires:           python3-requests-toolbelt
Requires:           python3-magic
Requires:           python3-ipython-console
Requires:           python3-six
Requires:           python3-pbr
Requires:           python3-defusedxml
%{?python_provide:%python_provide python3-%{distname}}

%description -n python3-%{distname}
A library to ease use of the JIRA 5 REST APIs.


%prep
%setup -q -n %{distname}-%{version}
%patch0 -p1

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

# Remove shebang in the non-executable files
sed -i -e '/^#!\//, 1d' %{modname}/{client,config,jirashell}.py


%build
%py3_build


%install
%py3_install

# No tests in PYPI package.
# %%check
# python3 -m pytest

%files -n python3-%{distname}
%doc PKG-INFO
%license LICENSE
%{_bindir}/jirashell
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{eggname}-%{version}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-6
- Add new BR of pbr.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Subpackage python2-jira has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Jul 17 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.15-3
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Ralph Bean <rbean@redhat.com> - 1.0.15-2
- Add missing deps.  https://bugzilla.redhat.com/show_bug.cgi?id=1589006

* Fri May 25 2018 Ralph Bean <rbean@redhat.com> - 1.0.15-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Nov 21 2016 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-1
- Update to 1.0.7 version
- Provide Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Ralph Bean <rbean@redhat.com> - 0.50-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Ralph Bean <rbean@redhat.com> - 0.13-7
- Fix upstream url for https://bugzilla.redhat.com/1285760

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Ralph Bean <rbean@redhat.com> - 0.13-5
- Change dep from the ipython meta package to just python-ipython-console.
- Move the /tools/ module into the jira namespace to avoid potential conflict.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Ralph Bean <rbean@redhat.com> - 0.13-3
- Patch out mime type detection as per review feedback.

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.13-2
- Modernize python2 rpm macros.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.13-1
- Initial package for Fedora
