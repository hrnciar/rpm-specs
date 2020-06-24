Name:           bmon
Version:        3.7
Release:        13%{?dist}
Summary:        Bandwidth monitor and rate estimator

License:        BSD and GPLv2
URL:            http://github.com/tgraf/bmon
Source0:        https://github.com/tgraf/bmon/releases/download/v%{version}/bmon-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libconfuse-devel libnl3-devel ncurses-devel

%description
bmon is a monitoring and debugging tool to capture networking related
statistics and prepare them visually in a human friendly way. It
features various output methods including an interactive curses user
interface and a programmable text output for scripting.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%{_bindir}/bmon
%{_mandir}/man8/bmon.8*
%{_docdir}/bmon/examples/bmon.conf

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.7-8
- libconfuse rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.7-5
- libconfuse rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Jon Ciesla <limburgher@gmail.com> - 3.7-3
- libconfuse rebuild.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.7-1
- Update to 3.7 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Thomas Graf <tgraf@suug.ch> - 3.6-1
- Update to 3.6 release

* Sat Aug 30 2014 Thomas Graf <tgraf@suug.ch> - 3.5-1
- Update to 3.5 release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 15 2013 Thomas Graf <tgraf@suug.ch> - 3.1-4
- Use install -p to preserve timestamp of non generated files

* Sun Sep 15 2013 Thomas Graf <tgraf@suug.ch> - 3.1-3
- Declare GPL license usage due to list.h
- Use version macro in spec file
- Enable verbose building via V=1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Thomas Graf <tgraf@suug.ch> - 3.1-1
- Initial release
