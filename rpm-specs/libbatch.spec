Name:           libbatch
Version:        2.4.2
Release:        3%{?dist}
Summary:        Generic batch management library

License:        LGPLv2
URL:            http://git.salome-platform.org/gitweb/?p=tools/libbatch.git
# Get source as follows
# $ git clone --branch V2_4_1 git://git.salome-platform.org/tools/libbatch.git
# $ rm -rf libbatch/.git
# $ tar cjf libbatch-2.4.1.tar.bz2 libbatch
Source0:        %{name}-%{version}.tar.bz2
# Use lib64 on x86_64
Patch0:         libbatch_libdir.patch
# Set a library soversion
Patch1:         libbatch_soversion.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# %%{_datadir}/cmake ownership
Requires:       cmake
# %%{_datadir}/autoconf ownership
Requires:       filesystem

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
%global __provides_exclude_from ^(%{python_sitearch}/.*\\.so|%{_datadir}/myapp/.*)$

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1


%build
export LDFLAGS='-Wl,--as-needed'
%cmake -DLIBBATCH_PYTHONPATH=%{python3_sitearch} .
%make_build


%install
%make_install

# Move autoconf macros to correct place
install -Dpm 0644 %{buildroot}%{_datadir}/%{name}/misc/check_libbatch.m4 %{buildroot}%{_datadir}/aclocal/check_libbatch.m4
rm -rf %{buildroot}%{_datadir}/%{name}


%ldconfig_scriptlets


%files
%license COPYING
%{_libdir}/%{name}.so.*
%{python3_sitearch}/_%{name}.so
%{python3_sitearch}/%{name}.py*
%{python3_sitearch}/__pycache__/%{name}.*

%files devel
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/aclocal/check_libbatch.m4
%{_libdir}/%{name}.so


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Sandro Mani <manisandro@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Tue Jul 17 2018 Sandro Mani <manisandro@gmail.com> - 2.4.0-3
- Switch to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Sandro Mani <manisandro@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 2.3.2-3
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 2.3.2-1
- Update to 2.3.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 06 2016 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-3
- Filter private libaries from Provides/Requires.
- Stop excessive linking (unused-direct-shlib-dependency).
- Add library soversion.

* Sun Feb 16 2014 Sandro Mani <manisandro@gmail.com> - 2.1.0-2
- Explicitly specify python2

* Sun Feb 16 2014 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Thu Oct 03 2013 Sandro Mani <manisandro@gmail.com> - 2.0.0-1.git20131003
- Initial package
