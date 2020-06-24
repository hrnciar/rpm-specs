Name:           hexer
Version:        1.0.5
Release:        1%{?dist}
Summary:        Interactive binary editor

License:        BSD
URL:            http://devel.ringlet.net/editors/hexer/
Source0:        http://devel.ringlet.net/files/editors/hexer/hexer-1.0.5.tar.xz

Patch1: error_msg_fix.patch

BuildRequires:	gcc
BuildRequires:  ncurses-devel

%description
Hexer is an interactive binary editor (also known as a hex-editor)
with a Vi-like interface. Its most important features are multiple buffers,
multiple-level undo, command-line editing with completion, and binary regular
expressions.

%prep
%setup -q

%patch1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}/
cp -p hexer %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p hexer.1 %{buildroot}%{_mandir}/man1/

%files
%doc README
%license COPYRIGHT
%{_bindir}/hexer
%{_mandir}/man1/hexer.1*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 - Alex Kashchenko <akashche@redhat.com> - 1.0.5-0
- updated sources to 1.0.5
- added error_msg_fix.patch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 - Alex Kashchenko <akashche@redhat.com> - 1.0.3-0
- updated sources to 1.0.3
- removed clang and gcc-c++ from build-requires

* Tue Feb 20 2018 - Jiri Vanek <jvanek@redhat.com> - 0.2.3-6
- added buildrequires on gcc/gcc-c++
- to follow new packaging guidelines which no longer automatically pulls gcc/c++ to build root

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 Alex Kashchenko <alex.kasko.mail@gmail.com> 0.2.3-1
- initial package
