%global commit 2066144

Name:          fst
Version:       1.9
Release:       0.15.20110131git%{commit}%{?dist}
Summary:       Run VST plugins under wine
License:       GPLv2+
URL:           http://www.joebutton.co.uk/fst/
Source0:       http://repo.or.cz/w/%{name}.git/snapshot/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires: gtk2-devel 
BuildRequires: jack-audio-connection-kit-devel 
BuildRequires: alsa-lib-devel
BuildRequires: wine-devel
BuildRequires: lash-devel
BuildRequires: wine-devel
ExclusiveArch: i686

%description
%{name} is an audio plugin host that allows you to run native Windows VST audio 
plugins DLL's under wine on Linux using the JACK audio connection kit.

%package devel
Summary:      Development files for fst
Requires:     %{name}%{?_isa} = %{version}-%{release}
%description devel 
Development headers for %{name} and VST plugins

%prep
%setup -q -n %{name}

%build
sed -i -e 's/\/local/\//' -e 's/\/lib/\/%{_lib}/' Makefile

make %{?_smp_mflags} LASH_EXISTS=no CFLAGS="%{optflags}" 
sed -i -e 's|exec "$WINELOADER" "$apppath" "$@"|exec "$WINELOADER" "%{_libdir}/fst/fst.exe.so" "$@"|' fst.exe

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -rp *.so %{buildroot}%{_libdir}/%{name}
cp -rp *.exe %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -rp *.h vestige %{buildroot}%{_includedir}/%{name}

%files
%doc COPYING README
%{_bindir}/*
%{_libdir}/%{name}

%files devel
%{_includedir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.15.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.14.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.13.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.12.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.11.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.10.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.9.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.8.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-0.7.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-0.6.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-0.5.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-0.4.20110131git2066144
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.9-0.3.20110131git
- various cleanups

* Fri Oct 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.9-0.2.20110131git2066144
- Add docs, smp_mflags
- Expand description

* Fri Oct 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.9-0.1.20110131git2066144
- Exclusive arch i686
- clean up sources and URLs

* Thu Oct 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.8-0.1.20110131git2066144
- Initial development

