# Conditional for release and snapshot builds.
# Uncomment for release-builds.
#global rel_build	1

# Settings used for build from git-snapshots.
%if 0%{?rel_build}
%global gittar		%{name}-%{version}.tar.gz
%else  # 0%%{?rel_build}
%global commit		597ce9fa42a5c11aa743c6bb3f45f57d2d395d9e
%global commit_date	20160309
%global shortcommit	%(c=%{commit};echo ${c:0:7})
%global gitver		git%{commit_date}-%{shortcommit}
%global gitrel		.git%{commit_date}.%{shortcommit}
%global gittar		%{name}-%{version}-%{gitver}.tar.gz
%endif # 0%%{?rel_build}

# Place rpm-macros into proper location.
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Setup _pkgdocdir.
%{!?_pkgdocdir:%global _pkgdocdir	%{_docdir}/lib%{name}-%{version}}
%{?_pkgdocdir:%global _pkgdocdir	%{_docdir}/lib%{name}}

# These macros are defined by macros-file in davel-pkg.
%global dynaplugz_datadir	%{_datadir}/%{name}
%global dynaplugz_plugindir	%{_libdir}/%{name}

# CMake-builds go out-of-tree.
%global cmake_builddir	build-%{?__isa}%{?dist}

# Fix 'W: unused-direct-shlib-dependency'.
%global __global_ldflags %(echo '%{?__global_ldflags} -Wl,--as-needed' | %{__sed} -e 's!^[ \t]\+!!g' -e 's![ \t]\+$!!g')

# Common description.
%global common_description						\
Dynamic plugin-loading like a boss.


Name:		dynaplugz
Version:	0.0.0.0
Release:	0.15%{?gitrel}%{?dist}
Summary:	Dynamic plugin-loading like a boss

License:	BSD
URL:		https://github.com/shogun-toolbox/%{name}
%if 0%{?rel_build}
Source0:	%{url}/archive/v%{version}.tar.gz#/%{gittar}
%else  # 0%%{?rel_build}
Source0:	%{url}/archive/%{commit}.tar.gz#/%{gittar}
%endif # 0%%{?rel_build}

%description
%{common_description}


%package -n lib%{name}
Summary:	Dynamic plugin-loading like a boss

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:	cmake
%else  # 0%%{?fedora} || 0%%{?rhel} > 7
BuildRequires:	cmake3
%endif # 0%%{?fedora} || 0%%{?rhel} > 7
BuildRequires:	gcc-c++				>= 4.4
BuildRequires:	hardlink
BuildRequires:	valgrind

Provides:	%{name}				== %{version}-%{release}
Provides:	%{name}%{?_isa}			== %{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} <= 25
Obsoletes:	%{name}				<= 0.0.0.0-0.2
%endif # 0%%{?fedora} && 0%%{?fedora} <= 25

%description -n lib%{name}
%{common_description}


%package -n lib%{name}-devel
Summary:	Development-files for %{name}

Requires:	lib%{name}%{?_isa}		== %{version}-%{release}
Requires:	rpm

Provides:	%{name}-devel			== %{version}-%{release}
Provides:	%{name}-devel%{?_isa}		== %{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} <= 25
Obsoletes:	%{name}-devel			<= 0.0.0.0-0.2
%endif # 0%%{?fedora} && 0%%{?fedora} <= 25

%description -n lib%{name}-devel
This package contains files to develop applications
using lib%{name}.


%package -n lib%{name}-doc
Summary:	Documentation-files for lib%{name}

BuildArch:	noarch

BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	perl-interpreter

Provides:	%{name}-doc			== %{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} <= 25
Obsoletes:	%{name}-doc			<= 0.0.0.0-0.2
%endif # 0%%{?fedora} && 0%%{?fedora} <= 25

%description -n lib%{name}-doc
This package contains documentation-files
for lib%{name}.


%prep
%setup -q%{?commit:n %{name}-%{commit}}
%{__mkdir} -p %{cmake_builddir}


%build
pushd %{cmake_builddir}
# Build using CMake3 on EPEL6 and EPEL7.
%if 0%{?fedora} || 0%{?rhel} > 7
%{cmake}								\
%else  # 0%%{?fedora} || 0%%{?rhel} > 7
%{cmake3}								\
%endif # 0%%{?fedora} || 0%%{?rhel} > 7
	-DCMAKE_BUILD_TYPE=RELEASE					\
	-DPROJECT_VERSION_GIT='%{?gitrel}'				\
	-DRPMMACROS_INSTALL_DIR='%{rpm_macros_dir}'			\
	..
%{_bindir}/doxygen -u doc/Doxyfile
%{__make} %{?_smp_mflags}

# Build the autodocs.
%{__make} doc
popd


%install
pushd %{cmake_builddir}
%{__make} install DESTDIR=%{buildroot}

# Install the autodocs.
%{__mkdir} -p %{buildroot}%{_pkgdocdir}
%{__cp} -a doc/html %{buildroot}%{_pkgdocdir}
popd

# Create symlink to tag-file.
/bin/ln -fs %{dynaplugz_datadir}/%{name}.tag				\
	%{buildroot}%{_pkgdocdir}/html

# Install other documentation.
for i in ChangeLog NEWS
do
	if [ ! -e "$i" ]
	then
		echo "dummy" > "$i"
	fi
done

%{__install} -pm 0644							\
	ChangeLog NEWS README.md					\
	%{buildroot}%{_pkgdocdir}

# Hardlink duplicate documentation-files.
%{_bindir}/hardlink -cv %{buildroot}%{_pkgdocdir}


%check
pushd %{cmake_builddir}
%{__make} memcheck
popd


%ldconfig_scriptlets -n lib%{name}


%files -n lib%{name}
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%license AUTHORS LICENSE.txt
%dir %{dynaplugz_datadir}
%dir %{dynaplugz_plugindir}
%{_libdir}/lib%{name}.so.*


%files -n lib%{name}-devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/NEWS
%{dynaplugz_datadir}/*
%{_includedir}/%{name}-%{version}%{?gitrel}
%{_libdir}/cmake
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{rpm_macros_dir}/macros.%{name}


%files -n lib%{name}-doc
# Pick up previously installed licenses.
%{?_licensedir:%license %{_datadir}/licenses/lib%{name}*}
%doc %{_pkgdocdir}
%dir %{dynaplugz_datadir}
%{dynaplugz_datadir}/%{name}.tag


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.15.git20160309.597ce9f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.14.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.13.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.0.0-0.12.git20160309.597ce9f
- Fix FTBFS - updated path of hardlink

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.11.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.10.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.9.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.8.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.7.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.6.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0.0-0.5.git20160309.597ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 09 2016 Björn Esser <fedora@besser82.io> - 0.0.0.0-0.4.git20160309.597ce9f
- add dynaplugz_(data|plugin)dir
- fix ownership of %%{dynaplugz_datadir}
- explicitly BR cmake3 on EPEL <= 7

* Wed Mar 09 2016 Björn Esser <fedora@besser82.io> - 0.0.0.0-0.3.git20160309.597ce9f
- new snapshot git20160309.597ce9f

* Wed Mar 09 2016 Björn Esser <fedora@besser82.io> - 0.0.0.0-0.2.git20160304.589c448
- split things in lib%%{name}-packages
- add conditionals for EPEL <= 7

* Fri Mar 04 2016 Björn Esser <fedora@besser82.io> - 0.0.0.0-0.1.git20160304.589c448
- initial rpm-release (#1314895)
