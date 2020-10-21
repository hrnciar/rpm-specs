#global commit 40746dae36452398649481fecad9cdc5f25cc80f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{name}-%{commit}
%else
%global source_folder %{name}-src-%{version}
%endif

Name:           qbs
# qbs was previously packaged as part of qt-creator, using the qt-creator version, hence the epoch bump
Epoch:          1
Version:        1.17.0
Release:        1%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Cross platform build tool

# See LGPL_EXCEPTION.txt
License:        LGPLv2 with exceptions and LGPLv3 with exceptions
URL:            https://wiki.qt.io/qbs
%if 0%{?commit:1}
Source0:        https://code.qt.io/cgit/qbs/qbs.git/snapshot/qbs-%{commit}.tar.xz
%else
Source0:        https://download.qt.io/official_releases/%{name}/%{version}/%{name}-src-%{version}.tar.gz
%endif

# qDebug output is silenced by default by the logging rules, but TestBlackboxQt::pluginMetaData
# relies in a qDebug output. Enabling qDebug output causes other tests to fail since they expect
# empty stderr... So just print the relevant output to stderr directly...
Patch0:         qbs_test_pluginMetaData.patch


BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qdoc
BuildRequires:  qt5-qhelpgenerator
BuildRequires:  qt5-qtscript-devel

# Needed for tests
BuildRequires:  glibc-static
BuildRequires:  libstdc++-static
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel


%description
Qbs is a tool that helps simplify the build process for developing projects
across multiple platforms. Qbs can be used for any software project, regardless
of programming language, toolkit, or libraries used.

Qbs is an all-in-one tool that generates a build graph from a high-level
project description (like qmake or CMake) and additionally undertakes the task
of executing the commands in the low-level build graph (like make).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        examples
Summary:        Example projects using %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description    examples
The %{name}-examples package contains example files for using %{name}.

%package        doc
Summary:        Documentation for %{name}
License:        GFDL
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.


%prep
%autosetup -p1 -n %{source_folder}


%build
%qmake_qt5 \
  QBS_INSTALL_PREFIX=%{_prefix} \
  QBS_LIBRARY_DIRNAME=%{_lib} \
  QBS_LIBEXEC_INSTALL_DIR=%{_libexecdir}/%{name} \
  QBS_RELATIVE_LIBEXEC_PATH=../libexec/%{name} \
  CONFIG+=qbs_enable_project_file_updates \
  CONFIG+=qbs_disable_rpath \
  CONFIG+=qbs_enable_unit_tests \
  CONFIG+=nostrip \
  QMAKE_LFLAGS="-Wl,--as-needed" \
  qbs.pro
# LD_LIBRARY_PATH: Because the qbs executable built is itself invoked, and it requires the built qbs libraries
LD_LIBRARY_PATH=%{_lib} %make_build
%make_build docs
%make_build html_docs


%install
make install INSTALL_ROOT=%{buildroot}
make install_docs INSTALL_ROOT=%{buildroot}

# Remove python dmgbuild code, it only works on macOS (#1559529)
rm -rf %{buildroot}%{_datadir}/qbs/python/mac_alias/
rm -rf %{buildroot}%{_datadir}/qbs/python/ds_store/
rm -rf %{buildroot}%{_datadir}/qbs/python/dmgbuild/
rm -rf %{buildroot}%{_datadir}/qbs/python/biplist/
rmdir %{buildroot}%{_datadir}/qbs/python/
rm -f %{buildroot}%{_libexecdir}/qbs/dmgbuild


%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%{buildroot}/%{_bindir}/qbs-setup-toolchains --detect
%{buildroot}/%{_bindir}/qbs-setup-qt %{_bindir}/qmake-qt5 qt5
%ifarch s390x ppc64le ppc64 aarch64 armv7hl
# TODO: Some tests fail with a timeout error on these arches
QBS_AUTOTEST_PROFILE=qt5 make check || :
%else
# TODO: This test results in a SIGBUS
# TestLanguage::nonRequiredProducts
QBS_AUTOTEST_PROFILE=qt5 make check || :
%endif


%ldconfig_scriptlets


%files
%license LICENSE.LGPLv21 LICENSE.LGPLv3 LGPL_EXCEPTION.txt
%doc README.md
%{_bindir}/%{name}*
%{_libdir}/%{name}/
%{_libdir}/libqbs*.so.1
%{_libdir}/libqbs*.so.1.17
%{_libdir}/libqbs*.so.1.17.*
%{_libexecdir}/qbs/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%exclude %{_datadir}/%{name}/examples

%files devel
%{_includedir}/%{name}/
%{_libdir}/libqbs*.so
%{_libdir}/libqbs*.prl

%files examples
%{_datadir}/%{name}/examples/

%files doc
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/%{name}.qch
%doc %{_docdir}/%{name}/html/

%changelog
* Mon Sep 07 2020 Marie Loise Nolden <loise@kde.org> - 1:1.17.0-1
- Update to 1.17.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Sandro Mani <manisandro@gmail.com> - 1:1.16.0-1
- Update to 1.16.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 1:1.15.0-1
- Update to 1.15.0

* Thu Nov 07 2019 Sandro Mani <manisandro@gmail.com> - 1:1.14.1-1
- Update to 1.14.1

* Thu Oct 10 2019 Sandro Mani <manisandro@gmail.com> - 1:1.14.0-1
- Update to 1.14.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Sandro Mani <manisandro@gmail.com> - 1:1.13.1-1
- Update to 1.13.1

* Tue Apr 16 2019 Sandro Mani <manisandro@gmail.com> - 1:1.13.0-1
- Update to 1.13.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.2-1
- Update to 1.12.2

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.1-1
- Update to 1.12.1

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.0-1
- Update to 1.12.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.0-0.3.git40746da
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.0-0.2.git40746da
- Add qbs_installheader.patch

* Thu Jun 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.12.0-0.1.git40746da
- Update to git 40746da

* Mon May 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.1-1
- Update to 1.11.1

* Wed Mar 28 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-1
- Update to 1.11.0

* Sun Mar 25 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.5.git8e39638
- Also remove %%{_libexecdir}/qbs/dmgbuild

* Fri Mar 23 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.4.git8e39638
- Remove python dmgbuild code, it only works on macOS (#1559529)

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.3.git8e39638
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.2.git8e39638
- Add patch to install missing header

* Wed Feb 07 2018 Sandro Mani <manisandro@gmail.com> - 1:1.11.0-0.1.git8e39638
- Update to git 8e39638

* Fri Dec 08 2017 Sandro Mani <manisandro@gmail.com> - 1:1.10.0-1
- Update to 1.10.0

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1:1.9.1-1
- Update to 1.9.1

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 1:1.9.0-1
- Update to 1.9.0

* Mon Jul 31 2017 Sandro Mani <manisandro@gmail.com> - 1:1.9.0-0.1.git998c698
- Update to latest git

* Sat Jul 29 2017 Sandro Mani <manisandro@gmail.com> - 1:1.8.1-2
- Add doc subpackage
- Enable tests

* Wed Jul 26 2017 Sandro Mani <manisandro@gmail.com> - 1:1.8.1-1
- Initial package
