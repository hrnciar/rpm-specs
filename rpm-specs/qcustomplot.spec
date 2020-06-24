# Bump this as appropriate when doing release updates, check i.e. with abi_compliance_checker
# First digit: major, bump when incompatible changes were performed
# Second digit: minor, bump when interface was extended
%global so_ver 2.0.0
#global pre beta

Name:           qcustomplot
Version:        2.0.1
Release:        5%{?pre:.%pre}%{?dist}
Summary:        Qt widget for plotting and data visualization

License:        GPLv3+
URL:            http://www.qcustomplot.com/
Source0:        http://www.qcustomplot.com/release/%{version}%{?pre:-%pre}/QCustomPlot.tar.gz
Source1:        %{name}.pro

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel


%description
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt4 version.


%package        devel
Summary:        Development files for %{name} (Qt4)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}  (Qt4).


%package        qt5
Summary:        Qt widget for plotting and data visualization
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt5 version.


%package        qt5-devel
Summary:        Development files for %{name} (Qt5)
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}  (Qt5).


%package        doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation and examples for
%{name}.


%prep
%autosetup -p1 -n %{name}
cp -a %{SOURCE1} .


%build
mkdir qt4
(
cd qt4
LDFLAGS="%{__global_ldflags} -Wl,--as-needed" %qmake_qt4 SOVERSION=%{so_ver} LIBDIR=%{_libdir} ..
%make_build
)

mkdir qt5
(
cd qt5
LDFLAGS="%{__global_ldflags} -Wl,--as-needed" %qmake_qt5 SOVERSION=%{so_ver} QTSUFFIX=-qt5 LIBDIR=%{_libdir} ..
%make_build
)


%install
make -C qt4 INSTALL_ROOT=%{buildroot} install
make -C qt5 INSTALL_ROOT=%{buildroot} install

# pkg-config file
install -d %{buildroot}%{_libdir}/pkgconfig/
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot
EOF

install -d %{buildroot}%{_libdir}/pkgconfig/
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}-qt5.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}-qt5
Description: %{summary}
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot-qt5
EOF

%ldconfig_scriptlets

%ldconfig_scriptlets qt5


%files
%license GPL.txt
%doc changelog.txt
%{_libdir}/libqcustomplot.so.*

%files devel
%{_includedir}/qcustomplot.h
%{_libdir}/libqcustomplot.so
%{_libdir}/pkgconfig/%{name}.pc

%files qt5
%license GPL.txt
%doc changelog.txt
%{_libdir}/libqcustomplot-qt5.so.*

%files qt5-devel
%{_includedir}/qcustomplot.h
%{_libdir}/libqcustomplot-qt5.so
%{_libdir}/pkgconfig/%{name}-qt5.pc

%files doc
%license GPL.txt
%doc documentation examples


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 2.0.0-1
- Update to 2.0.0
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Sandro Mani <manisandro@gmail.com> - 2.0.0-0.1.beta
- Update to 2.0.0-beta

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Sandro Mani <manisandro@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Sandro Mani <manisandro@gmail.com> - 1.3.1-3
- Fix qcustomplot-qt5.pc

* Wed Apr 29 2015 Sandro Mani <manisandro@gmail.com> - 1.3.1-2
- Also build a qt5 version

* Sat Apr 25 2015 Sandro Mani <manisandro@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Sun Dec 28 2014 Sandro Mani <manisandro@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Fri Dec 19 2014 Sandro Mani <manisandro@gmail.com> - 1.2.1-2
- BuildRequires: qt-devel -> qt4-devel
- Use %%license
- Don't abuse version as so version
- Use -Wl,--as-needed

* Sat Aug 09 2014 Sandro Mani <manisandro@gmail.com> - 1.2.1-1
- Initial package
