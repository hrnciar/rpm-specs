Name:		open-amp
Version:	2020.04.0
Release:	2%{?dist}
Summary:	Open Asymmetric Multi Processing (OpenAMP) framework project

License:	BSD
URL:		https://github.com/OpenAMP/open-amp/
Source0:	https://github.com/OpenAMP/open-amp/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	libmetal-devel
BuildRequires:	libsysfs-devel

%description
The OpenAMP framework provides software components that enable development of
software applications for Asymmetric Multiprocessing (AMP) systems.

%package devel
Summary:	Development files for OpenAMP
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for OpenAMP
baremetal, and RTOS environments.


%prep
%autosetup


%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INCLUDE_PATH=%{_includedir}/libmetal/ \
	-DCMAKE_LIBRARY_PATH=%{_libdir} \
	-DWITH_STATIC_LIB=OFF \
	-DWITH_APPS=ON ..
%make_build


%install
cd build
%make_install

%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.md
%{_bindir}/matrix_multiply-shared
%{_bindir}/matrix_multiplyd-shared
%{_bindir}/msg-test-rpmsg-flood-ping-shared
%{_bindir}/msg-test-rpmsg-ping-shared
%{_bindir}/msg-test-rpmsg-update-shared
%{_bindir}/rpc_demod-shared
%{_bindir}/rpmsg-echo-ping-shared
%{_bindir}/rpmsg-echo-shared
%{_bindir}/rpmsg-sample-echo-shared
%{_bindir}/rpmsg-sample-ping-shared
%{_libdir}/libopen_amp.so.0
%{_libdir}/libopen_amp.so.0.1.0


%files devel
%{_includedir}/openamp/
%{_libdir}/libopen_amp.so


%changelog
* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04.0-1
- Update to 2020.04.0

* Thu Mar 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.01.0-1
- Update to 2020.01.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2018.10-1
- Update to 2018.10 release

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2018.04-1
- Update to 2018.04 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-2
- Minor fixues for package review

* Fri Feb 16 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2017.10-1
- Initial packaging
