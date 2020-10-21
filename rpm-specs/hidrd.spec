%global git_commit 7e94881a6059a824efaed41301c4a89a384d86a2
%global git_date 20180117

%global git_short_commit %(c=%{git_commit}; echo ${c:0:8})
%global git_suffix %{git_date}git%{git_short_commit}

Name:		hidrd
Version:	0.2.0
Release:	13.%{git_suffix}%{?dist}
Summary:	HID report descriptor I/O library and conversion tool
License:	GPLv2+
URL:		https://github.com/DIGImend/hidrd
Source0:	https://github.com/DIGImend/hidrd/archive/%{git_commit}.tar.gz#/%{name}-%{version}-%{git_suffix}.tar.gz
BuildRequires:	gcc, make, automake, autoconf, libtool, libxml2-devel

%package devel
Summary:	Development files needed for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%description
Hidrd is a library and a tool for reading, writing and converting HID report
descriptors in/between various formats.

%prep
%autosetup -n %{name}-%{git_commit}
./bootstrap

%build
%configure
# fix unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%check
make check

%install
%make_install
# remove .a/.la files
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/hidrd-convert
%{_libdir}/lib%{name}*.so.*
%{_datadir}/xml

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13.20180117git7e94881a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12.20180117git7e94881a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11.20180117git7e94881a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10.20180117git7e94881a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9.20180117git7e94881a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8.20180117git7e94881a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.0-7.20180117git7e94881
- New version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6.20160712git1abf7033
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5.20160712git1abf7033
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.20160712git1abf7033
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 20 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.0-3.20160712git1abf7033
- Fixed unused-direct-shlib-dependency

* Tue Jul 19 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.0-2.20160712git1abf7033
- Fixed according to Fedora review

* Tue Jul 12 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.0-1.20160712git1abf7033
- Initial version
