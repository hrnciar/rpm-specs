Name:           samurai
Version:        1.1
Release:        1%{?dist}
Summary:        ninja-compatible build tool written in C

License:        ASL 2.0
URL:            https://github.com/michaelforney/samurai
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

%description
samurai is a ninja-compatible build tool written in C99
with a focus on simplicity, speed, and portability.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix} MANDIR=%{_mandir}

%files
%license LICENSE
%doc README.md
%{_bindir}/samu
%{_mandir}/man1/samu.1*

%changelog
* Sat May 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1-1
- Initial package
