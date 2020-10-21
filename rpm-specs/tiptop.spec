Name:           tiptop
Version:        2.3.1
Release:        13%{?dist}
Summary:        Performance monitoring tool based on hardware counters
License:        GPLv2

URL:            http://tiptop.gforge.inria.fr/
Source0:        http://tiptop.gforge.inria.fr/releases/tiptop-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel

%description
Hardware performance monitoring counters have recently received a lot of
attention. They have been used by diverse communities to understand and
improve the quality of computing systems: For example, architects use them to
extract application characteristics and propose new hardware mechanisms;
compiler writers study how generated code behaves on particular hardware;
software developers identify critical regions of their applications and
evaluate design choices to select the best performing implementation. We
propose that counters be used by all categories of users, in particular
non-experts, and we advocate that a few simple metrics derived from these
counters are relevant and useful. For example, a low IPC (number of executed
instructions per cycle) indicates that the hardware is not performing at its
best; a high cache miss ratio can suggest several causes, such as conflicts
between processes in a multicore environment.

Tiptop is a performance monitoring tool for Linux. It provides a dynamic
real-time view of the tasks running in the system. Tiptop is very similar to
the top utility, but most of the information displayed comes from hardware
counters.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS README tiptoprc
%license COPYING
%{_bindir}/*tiptop
%{_mandir}/man1/*tiptop.1*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.3.1-7
- BR: gcc after https://fedoraproject.org/wiki/Packaging:C_and_C++ update

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1
- Drop tiptop-sigfpe.patch (BZ 1141338)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.3-3
- Patch for BZ 1141338

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Christopher Meng <rpm@cicku.me> - 2.3-1
- Update to 2.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct  5 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-3
- Add patch to support aarch64

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Christopher Meng <rpm@cicku.me> - 2.2-1
- Update to 2.2

* Sat Nov 10 2012 Christopher Meng <rpm@cicku.me> - 2.1-1
- Initial Package.
