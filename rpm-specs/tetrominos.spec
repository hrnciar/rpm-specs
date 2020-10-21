Name:           tetrominos
Version:        1.0.1
Release:        7%{?dist}
Summary:        Simple CLI logical game
Summary(cs):    Jednoduchá terminálová logická hra

License:        MIT
URL:            https://github.com/sparkoo/NTetris
Source0:        https://github.com/sparkoo/NTetris/archive/%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
Requires:       ncurses

%description
Build tetromino blocks to fill full lines. Based on Ncurses lib for CLI gaming.

%description -l cs
Postavte tetromino bloky tak, aby zaplnily celé řádky.

%prep
%setup -q -n NTetris-%{version}

%build
make clean
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags} -Wl,--build-id=sha1"
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}
mv %{buildroot}%{_bindir}/ntetris %{buildroot}%{_bindir}/%{name}


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb  8 2017 Michal Vala <mvala@redhat.com> 1.0.1-1
- initial version created many years ago as a school project
