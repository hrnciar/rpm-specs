Name:           jsl
Version:        0.3.0
Release:        24%{?dist}
Summary:        Check JavaScript code for common mistakes

License:        MPLv1.1
URL:            http://javascriptlint.com/
Source0:        http://javascriptlint.com/download/%{name}-%{version}-src.tar.gz
Patch0:         jsl-0.3.0-smash.patch
Patch1:         jsl-0.3.0-tests.patch
Patch2:         jsl-0.3.0-cflags.patch
BuildRequires:  gcc
BuildRequires:  readline-devel
BuildRequires:  perl-interpreter

%description
With JavaScript Lint, you can check all your JavaScript source code for
common mistakes without actually running the script or opening the web page.

JavaScript Lint holds an advantage over competing lints because it is based
on the JavaScript engine for the Firefox browser. This provides a robust
framework that can not only check JavaScript syntax but also examine the
coding techniques used in the script and warn against questionable
practices.


%prep
%setup -q
%patch0 -p1 -b .smash
%patch1 -p1 -b .tests
%patch2 -p1 -b .cflags


%build
# Fix DOS-y EOL encoding and permissions
find . -type f |xargs sed -i 's/\r//' $FILES
find . -type f |xargs chmod 644 $FILES

# Dependencies dealt with poorly -- no _smp_mflags
make -C src -f Makefile.ref SHARED_LIBRARY= \
        OBJDIR=. JS_EDITLINE=1 XCFLAGS="%{optflags}" \
	JS_READLINE=1 JS_EDITLINE=0 \
        OS_CFLAGS="-DXP_UNIX -DHAVE_VA_COPY -DVA_COPY=va_copy"


%install
install -d %{buildroot}%{_bindir}
install src/jsl %{buildroot}%{_bindir}


%check
cd tests
perl run_tests.pl ../src/jsl


%files
%{_bindir}/jsl


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-22
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-15
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.3.0-10
- Drop use of bundled editline, use readline instead
- Don't let the compiler warnings break build

* Wed Dec 04 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.3.0-9
- Fix build with -Werror=format-security

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.3.0-8
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.3.0-1
- Initial packaging
