Name:           hot-tux
Version:        0.3.1
Release:        10%{?dist}
Summary:        Graphical CPU utilization monitoring utility

License:        Artistic clarified
URL:            https://github.com/judovana/hot-tux
Source0:        https://github.com/judovana/hot-tux/archive/%{name}-%{version}.tar.gz
Patch1:         makefile.patch

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  coreutils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

%description
%{summary}.

%prep
%autosetup -n %{name}-%{name}-%{version}
# Drop docfiles manipulation (installation)
sed -i -e "/DOC/d" Makefile

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE copyright
%doc NEWS config.example CONTRIBUTORS
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 16 2016 Jiri Vanek <jvanek@redhat.com> - 0.3.1-1
- Initial package
