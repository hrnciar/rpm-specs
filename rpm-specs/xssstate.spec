Name:          xssstate
Version:       1.1
Release:       15%{?dist}
Summary:       A simple tool to retrieve the X screen saver state
License:       MIT
URL:           http://tools.suckless.org/%{name}
Source0:       http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: libXScrnSaver-devel
BuildRequires: make
BuildRequires: sed

%description
%{summary}.

%prep
%setup -q
sed -e 's|PREFIX = /usr/local|PREFIX = %{_prefix}|' \
    -e 's|LIBS = -L/usr/lib -lc -lX11 -lXss|LIBS = -L%{_libdir} -lc -lX11 -lXss|' \
    -e 's|CFLAGS = -g -std=c99 -pedantic -Wall -O0 ${INCS} ${CPPFLAGS}|CFLAGS = %{optflags} ${INCS} ${CPPFLAGS}|' \
   -i config.mk
sed -i 's|^\t@|\t|' Makefile
chmod -x xsidle.sh

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc LICENSE README xsidle.sh
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Petr Šabata <contyk@redhat.com> - 1.1-11
- Adding missing build dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Petr Šabata <contyk@redhat.com> - 1.1-1
- 1.1 bump (format patch included)

* Tue May 07 2013 Petr Šabata <contyk@redhat.com> - 1.0-1
- Initial package.
