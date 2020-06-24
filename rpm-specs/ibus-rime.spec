Name:           ibus-rime
Version:        1.4.0
Release:        3%{?dist}
Summary:        Rime Input Method Engine for IBus
Summary(zh):    中州韻輸入法引擎

License:        GPLv3
URL:            https://rime.im/
Source0:        https://github.com/rime/ibus-rime/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         ibus-rime-1.4.0-fixes-compile.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig, cmake
BuildRequires:  librime-devel >= 1.2
BuildRequires:  ibus-devel, libnotify-devel
BuildRequires:  brise >= 0.35
Requires:       brise >= 0.35

%description
ibus-rime: Rime Input Method Engine for IBus

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.


%description -l zh
中州韻輸入法引擎

中州韻輸入法引擎，思想用鍵盤表達也行。

Rime 預設輸入方案有：朙月拼音、語句流、倉頡、速成、五筆、雙拼、
地球拼音、注音、粵拼、吳語、中古漢語拼音、五筆畫、國際音標等。

%prep
%setup -q
%patch0 -p1 -b .compile


%build
%cmake
make VERBOSE=1 %{?_smp_mflags}


%install
sed -i -e "s'/usr/lib/ibus-rime/ibus-engine-rime'%{_libexecdir}/ibus-engine-rime'" rime.xml

mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/
install -p -m 0755 ibus-engine-rime $RPM_BUILD_ROOT/%{_libexecdir}/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/ibus/component/
install -p -m 0644 rime.xml $RPM_BUILD_ROOT/%{_datadir}/ibus/component/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/ibus-rime/icons/
install -p -m 0644 icons/*.png $RPM_BUILD_ROOT/%{_datadir}/ibus-rime/icons/


%files
%doc README.md LICENSE CHANGELOG.md
%{_libexecdir}/ibus-engine-rime
%{_datadir}/ibus/component/rime.xml
%{_datadir}/ibus-rime/


%changelog
* Fri Feb  7 2020 Peng Wu <pwu@redhat.com> - 1.4.0-3
- Fixes FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Peng Wu <pwu@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Peng Wu <pwu@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan  6 2015 Peng Wu <pwu@redhat.com> - 1.2-1
- Update to 1.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Peng Wu <pwu@redhat.com> - 1.1-1
- Update to 1.1

* Mon Dec  9 2013 Peng Wu <pwu@redhat.com> - 1.0-1
- Update to 1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Peng Wu <pwu@redhat.com> - 0.9.9-2
- Fixes the spec

* Thu May  9 2013 Peng Wu <pwu@redhat.com> - 0.9.9-1
- The Initial Version

