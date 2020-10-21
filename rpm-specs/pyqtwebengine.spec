
%if 0%{?fedora} || 0%{?rhel} > 6
%global with_python3 1
%endif
%if 0%{?fedora} < 31
%global with_python2 1
%endif

Summary: Python bindings for QtWebEngine
Name:    pyqtwebengine
Version: 5.15.0
Release: 2%{?dist}

License: GPLv3
Url:     https://www.riverbankcomputing.com/software/pyqt/
#Source0: https://www.riverbankcomputing.com/static/Downloads/PyQtWebEngine/%{version}/PyQtWebEngine_gpl-%{version}.tar.gz
Source0: https://files.pythonhosted.org/packages/0d/8d/aece7598d2959f66f09fcced6487dd7727f44ad867fc09978c5aeeaf1d29/PyQtWebEngine-5.15.0.tar.gz
ExclusiveArch: %{qt5_qtwebengine_arches}

## downstream patches
Patch100: PyQtWebEngine-Timeline.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5WebEngine)

%global sip_ver 4.19.14
%if 0%{?with_python2}
BuildRequires: python2-devel python2
BuildRequires: python2-qt5
BuildRequires: python2-qt5-devel
BuildRequires: python2-pyqt5-sip >= %{sip_ver}
BuildRequires: python2-sip-devel >= %{sip_ver}
%endif
%if 0%{?with_python3}
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}
BuildRequires: python%{python3_pkgversion}-qt5
BuildRequires: python%{python3_pkgversion}-qt5-devel
BuildRequires: python%{python3_pkgversion}-pyqt5-sip >= %{sip_ver}
BuildRequires: python%{python3_pkgversion}-sip-devel >= %{sip_ver}
%endif # with_python3

%description
%{summary}.

%package -n python2-qt5-webengine
Summary: Python bindings for Qt5 WebEngine
Requires:  python2-qt5%{?_isa}
%{?python_provide:%python_provide python2-qt5-webengine}
%description -n python2-qt5-webengine
%{summary}.

%package -n python%{python3_pkgversion}-qt5-webengine
Summary: Python3 bindings for Qt5 WebEngine
Requires:  python%{python3_pkgversion}-qt5%{?_isa}
%{?python_provide:%python_provide python%{python3_pkgversion}-qt5-webengine}
%description -n python%{python3_pkgversion}-qt5-webengine
%{summary}.

%package devel
Summary: Development files for %{name}
# when webengine content was split out
Conflicts: python2-qt5-devel < 5.12.1
Conflicts: python%{python3_pkgversion}-qt5-devel < 5.12.1
Requires: sip
BuildArch: noarch
%description devel
%{summary}.

%package doc
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.


%prep
%setup -q -n PyQtWebEngine-%{version}

%patch100 -p1 -b .Timeline


%build
PATH=%{_qt5_bindir}:$PATH ; export PATH

# Python 2 build:
%if 0%{?with_python2}
mkdir %{_target_platform}
pushd %{_target_platform}
%{__python2} ../configure.py \
  --qmake=%{_qt5_qmake} \
  --verbose \
  QMAKE_CFLAGS_RELEASE="%{build_cflags}" \
  QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}" \
  QMAKE_LFLAGS_RELEASE="%{build_ldflags}"

%make_build
popd
%endif # with_python2

# Python 3 build:
%if 0%{?with_python3}
mkdir %{_target_platform}-python3
pushd %{_target_platform}-python3
%{__python3} ../configure.py \
  --qmake=%{_qt5_qmake} \
  --verbose \
  QMAKE_CFLAGS_RELEASE="%{build_cflags}" \
  QMAKE_CXXFLAGS_RELEASE="%{build_cxxflags}" \
  QMAKE_LFLAGS_RELEASE="%{build_ldflags}"

%make_build
popd
%endif # with_python3


%install

# Python 3 build:
%if 0%{?with_python3}
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-python3

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python3_sitearch}/PyQt5/*.so ; do
test -x $i  || chmod a+rx $i
done
%endif # with_python3

# Python 2 build:
%if 0%{?with_python2}
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python2_sitearch}/PyQt5/*.so ; do
test -x $i  || chmod a+rx $i
done

%endif # with_python2


%if 0%{?with_python2}
%files -n python2-qt5-webengine
%doc README
%license LICENSE
%{python2_sitearch}/PyQtWebEngine-%{version}.dist-info/
%{python2_sitearch}/PyQt5/QtWebEngine.*
%{python2_sitearch}/PyQt5/QtWebEngineCore.*
%{python2_sitearch}/PyQt5/QtWebEngineWidgets.*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-qt5-webengine
%doc README
%license LICENSE
%{python3_sitearch}/PyQtWebEngine-%{version}.dist-info/
%{python3_sitearch}/PyQt5/QtWebEngine.*
%{python3_sitearch}/PyQt5/QtWebEngineCore.*
%{python3_sitearch}/PyQt5/QtWebEngineWidgets.*
%endif

%files devel
%license LICENSE
%{_datadir}/sip/PyQt5/QtWebEngine*/

%files doc
# avoid dep on qscintilla-python, own %%_qt5_datadir/qsci/... here for now
%dir %{_qt5_datadir}/qsci/
%dir %{_qt5_datadir}/qsci/api/
%dir %{_qt5_datadir}/qsci/api/python/
%doc %{_qt5_datadir}/qsci/api/python/PyQtWebEngine.api


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.15.0-1
- 5.15.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.14.0-2
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.0-1
- 5.14.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.13.1-1
- 5.13.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.12.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-5
- fix/workaround -debug generation
- +python2 support on f30

* Thu Apr 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-4
- -devel: %%license LICENSE

* Wed Apr 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-3
- %%doc README
- %%license LICENSE
- -devel: Requires: sip
- use %%autosetup

* Wed Apr 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-2
- update Source0 URL
- use ExclusiveArch
- use %%build_cflags %%build_cxxflags %%build_ldflags
- BR: gcc-c++

* Sat Mar 23 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- first try

