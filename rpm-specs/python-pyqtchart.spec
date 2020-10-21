%global pypi_name PyQtChart

Name:           python-pyqtchart
Version:        5.15.0
Release:        3%{?dist}
Summary:        Set of Python bindings for The Qt Charts library
License:        GPLv3
URL:            https://www.riverbankcomputing.com/software/pyqtchart/
Source0:        %pypi_source

BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-sip-devel
BuildRequires:  qt5-qtcharts-devel
# as of 2020-04-18, depends on libQt5Charts.so.5(Qt_5.14.2_PRIVATE_API)(64bit)
BuildRequires:  qt5-qtbase-private-devel

%global distinfo %{python3_sitearch}/PyQtChart-%{version}.dist-info

%description
PyQtChart is a set of Python bindings for The Qt Company's Qt Charts library.
The bindings sit on top of PyQt5 and are implemented as a single module.


%package -n python3-pyqtchart
Summary:    %{summary}
%{?python_provide:%python_provide python3-pyqtchart}
Requires:   python3-qt5
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}

%description -n python3-pyqtchart
PyQtChart is a set of Python 3 bindings for The Qt Company's Qt Charts library.
The bindings sit on top of PyQt5 and are implemented as a single module.


%package -n python3-pyqtchart-devel
Summary:    Development files for PyQtChart
%{?python_provide:%python_provide python3-pyqtchart-devel}
Requires:   python3-pyqtchart%{_isa} == %{version}-%{release}
# For the directories:
Requires:   python3-qt5-devel
Requires:   python3-qscintilla-qt5

%description -n python3-pyqtchart-devel
Development files for PyQtChart, such as sip files.


%prep
%autosetup -p1 -n PyQtChart-%{version}


%build
%set_build_flags
%{__python3} ./configure.py --qmake="%{_qt5_qmake}" --verbose
%make_build CXXFLAGS="%{optflags} -fPIC \$(DEFINES)"


%install
%make_install INSTALL_ROOT=%{buildroot}

# Make sure all modules are executable for RPM to get their dependencies, debuginfo, etc.
chmod a+rx %{buildroot}%{python3_sitearch}/PyQt5/*.so

%check
# Make sure we don't leak buildroot to dist-info
! grep %{buildroot} %{buildroot}%{distinfo}/*


%files -n python3-pyqtchart
%license LICENSE
%doc ChangeLog NEWS README
%{python3_sitearch}/PyQt5/QtChart.*
%{distinfo}/

%files -n python3-pyqtchart-devel
%{_datadir}/qt5/qsci/api/python/PyQtChart.api
%{_datadir}/sip/PyQt5/QtChart/


%changelog
* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 5.15.0-3
- rebuild (qt5)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 5.15.0-1
- Update to 5.15.0 (#1825487)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.13.1-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Miro Hrončok <mhroncok@redhat.com> - 5.13.1-1
- Update to 5.13.1

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.12-8
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.12-6
- drop BR: qt5-devel (convenience virtual dep only, packages should not use)
- BR: qt5-qtbase-private-devel (track private api usage)
- add explicit versioned dep on python3-pyqt5-sip-api
- drop explicit Requires: qt5-qtbase (rely on rpm autodeps)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.12-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Miro Hrončok <mhroncok@redhat.com> - 5.12-3
- Fix Python modules permissions to properly fix (#1731656)

* Sat Jul 20 2019 Miro Hrončok <mhroncok@redhat.com> - 5.12-2
- Add explicit runtime dependency on qt5-qtcharts (#1731656)

* Mon Jul 15 2019 Miro Hrončok <mhroncok@redhat.com> - 5.12-1
- Update to 5.12

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 5.11.1-2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 5.11.1-1
- Initial package
