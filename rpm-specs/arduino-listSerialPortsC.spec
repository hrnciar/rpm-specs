%global shortname listSerialPortsC

Name:		arduino-%{shortname}
Version:	1.4.0
Release:	8%{?dist}
Summary:	Simple multiplatform program to list serial ports with vid/pid/iserial fields
License:	LGPLv3+
URL:		http://www.arduino.cc
Source0:	https://github.com/arduino/listSerialPortsC/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz
BuildRequires:	libserialport-devel, java-devel
BuildRequires:	gcc

%description
Simple environment to test libserialport in a single build machine fashion.

%prep
%setup -q -n %{shortname}-%{version}

%build
gcc `pkg-config --cflags libserialport` %{optflags} main.c `pkg-config --libs libserialport` -o listSerialC
gcc `pkg-config --cflags libserialport` %{optflags} jnilib.c -I/usr/lib/jvm/java/include/ -I/usr/lib/jvm/java/include/linux -shared -fPIC `pkg-config --libs libserialport` -o liblistSerialsj.so

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 listSerialC %{buildroot}%{_bindir}
# Yes, this is not normal, but this isn't really a useful lib, it's only for arduino.
mkdir -p %{buildroot}%{_datadir}/arduino/lib/
install -m755 liblistSerialsj.so %{buildroot}%{_datadir}/arduino/lib/

%files
%license LICENSE.md
%doc README.md
%{_bindir}/listSerialC
%{_datadir}/arduino/lib/liblistSerialsj.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.4.0-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Tom Callaway <spot@fedoraproject.org> - 1.4.0-1
- initial package
