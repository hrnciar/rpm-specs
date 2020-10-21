%global sum    An extensible i3status wrapper written in python

%bcond_without doc
# test are somehow broken, so it's disabled now
%bcond_with    test

Name:           py3status
Version:        3.24
Release:        4%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/ultrabug/py3status
Source0:        https://github.com/ultrabug/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with doc}
BuildRequires:  dejavu-sans-mono-fonts
BuildRequires:  python3-sphinx
BuildRequires:  python3-fonttools
BuildRequires:  python3-pillow
%endif # docs
%if %{with test}
BuildRequires:  python3-tox
%endif #test
Requires:       i3status

%description
Using py3status, you can take control of your i3bar easily by:
- writing your own modules and have their output displayed on your bar
- handling click events on your i3bar and play with them in no time
- seeing your clock tick every second whatever your i3status interval
No extra configuration file needed, just install & enjoy !


%if %{with doc}
%package doc
Summary:         Documentation files for %{name}
BuildArch:       noarch

%description doc
%{sum}.
%endif #doc

%prep
%setup -q -n py3status-%{version}


%build
%py3_build

%if %{with doc}
# we have to build docs in doc dir because of hardcoded paths
pushd doc
export PYTHONPATH=..
sphinx-build-3 -d ../buildtree . ../html
popd
%{__rm} -rf html/.buildinfo
%endif # doc


%install
%py3_install


%if %{with test}
%check
tox
%endif # test

%files
%license LICENSE
%doc README.rst CHANGELOG
%{_bindir}/py3-cmd
%{_bindir}/py3status
%dir %{python3_sitelib}/py3status
%{python3_sitelib}/py3status/*
%{python3_sitelib}/*.egg-info

%if %{with doc}
%files doc
%license LICENSE
%doc html/
%endif # doc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.24-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.24-1
- Upgrade to version 3.24

* Sun Jan 05 2020 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.23-1
- Upgrade to version 3.23

* Wed Oct 23 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.21-1
- Upgrade to version 3.21

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.19-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.19-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.19-1
- Upgrade to version 3.19

* Wed Feb 20 2019 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.16-1
- Upgrade to version 3.16

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.12-1
- Update to new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.11-1
- Update to new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.9-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.9-1
- Update to new version

* Mon Apr 16 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.8-1
- Update to new version (BZ#1563227)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6-4
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.5-2
- don't build -doc subpackage for F25, there is a weird error

* Thu Aug 24 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.5-1
- update to version 3.6
- add -doc subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.5-1
- update to version 3.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3-2
- Rebuild for Python 3.6

* Sun Nov 20 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.3-1
- update to version 3.3

* Thu Nov 03 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.2-1
- update to version 3.2

* Thu Sep 15 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.1-1
- update to version 3.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 27 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 3.0-1
- update to version 3.0

* Thu Apr 21 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.9-1
- update to version 2.9
- use python3 support as default (BZ#1282483)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.7-1
- update to version 2.7

* Mon Aug 31 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.6-2
- fix modules location, it won't be used in %%doc anymore

* Mon Aug 31 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.6-1
- update to version 2.6

* Tue Aug 25 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.5-1
- update to version 2.5

* Thu Jul 16 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.4-1
- update to version 2.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.2-2
- move modules dir into docs

* Thu Jan 22 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.2-1
- update to new version

* Mon Oct 27 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.6-1
- inital package
