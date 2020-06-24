Name:           toilet
Version:        0.3
Release:        7%{?dist}
Summary:        Display large colorful characters in text mode

License:        WTFPL
URL:            http://caca.zoy.org/wiki/toilet
Source0:        http://caca.zoy.org/raw-attachment/wiki/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libcaca-devel

%description
The TOIlet project attempts to create a free replacement for the FIGlet
utility. TOIlet stands for "The Other Implementation’s letters", coined after
FIGlet's "Frank, Ian and Glen’s letters".


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc README ChangeLog NEWS TODO
%{_bindir}/%{name}
%{_datadir}/figlet
%{_mandir}/man1/toilet.1*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Iliana Weller <ilianaw@buttslol.net> - 0.3-2
- Spec cleanups

* Tue Dec  5 2017 Iliana Weller <ilianaw@buttslol.net> - 0.3-1
- Initial package build
