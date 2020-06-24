Name:           kismon
Version:        0.8.1
Release:        14%{?dist}
Summary:        A simple GUI client for kismet

License:        BSD
URL:            https://www.salecker.org/software/kismon.html
Source0:        https://files.salecker.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       kismet
Requires:       osm-gps-map-gobject
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       python3-simplejson
    
%description
Kismon is a PyGTK Kismet Newcore client that creates a live map of the
networks. 

%prep
%setup -q
for lib in %{name}/*.py %{name}/windows/*.py; do
    sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
    touch -r $lib $lib.new &&
    mv $lib.new $lib
done
chmod -x files/kismon.desktop

%build
%py3_build

%install
%py3_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README NEWS
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-14
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-8
- Require python3-gobject instead of python2-gobject

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuild for Python 3.6

* Mon Oct 30 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.1-1
- Update to new upstream version 0.8.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.7-1
- Update to new upstream version 0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-7
- osm-gps-map is the replacement for python-osmgpsmap

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-4
- Drop pyclutter because of its retirement in Fedora

* Wed Oct 03 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-3
- Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- COPYING added
- Patch0 is now upstream
- Update to new upstream version 0.6

* Mon May 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-2
- License fixed
- Old stuff removed

* Tue Mar 27 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-1
- Initial package for Fedora
