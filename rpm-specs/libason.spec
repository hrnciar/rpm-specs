Name:           libason
Version:        0.1.2
Release:        14%{?dist}
Summary:        A library for manipulating ASON values

License:        GPLv3+
URL: https://github.com/sadmac7000/libason
Source0: https://sadmac.fedorapeople.org/libason-0.1.2.tar.xz
Patch0: doc-fix-install-hook.patch

BuildRequires:  gcc
BuildRequires:  lemon, readline-devel

%description
ASON is an extension of JSON which specifies a semantic, and allows for pattern
expressions that can specify or match groups of JSON values. libason is a
simple library for manipulating ASON programmatically in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

for i  in `find $RPM_BUILD_ROOT/%{_mandir} -type l`; do
	ln -f -r -s `readlink $i` $i
done

%ldconfig_scriptlets


%files
%doc COPYING
%{_libdir}/*.so.*
%{_bindir}/asonq
%{_mandir}/man1/*

%files devel
%doc COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-12
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1.2-5
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 6 2014 Casey Dahlin <casey.dahlin@gmail.com> - 0.1.2-2
- Add --disable-silent-rules

* Thu Oct 2 2014 Casey Dahlin <casey.dahlin@gmail.com> - 0.1.2-1
- Update to latest upstream

* Sun Sep 28 2014 Casey Dahlin <casey.dahlin@gmail.com> - 0.1.1-1
- Initial packaging
