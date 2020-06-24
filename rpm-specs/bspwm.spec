Name:		bspwm
Version:	0.9.9
Release:	2%{?dist}
Summary:	A tiling window manager based on binary space partitioning

License:	BSD
URL:		https://github.com/baskerville/bspwm
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	desktop-file-utils


%description
bspwm is a tiling window manager that represents windows as the leaves of a
full binary tree.

It only responds to X events, and the messages it receives on a dedicated
socket.

bspc is a program that writes messages on bspwm's socket.

bspwm doesn't handle any keyboard or pointer inputs: a third party program
(e.g. sxhkd) is needed in order to translate keyboard and pointer events to
bspc invocations.


%prep
%setup -q


%build
make VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" \
	LDFLAGS="%{?__global_ldflags}"


%install
%make_install PREFIX="%{_prefix}"


%check
desktop-file-validate %{buildroot}/%{_datadir}/xsessions/%{name}.desktop


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/bspc
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/bspc.1.gz
%{_datadir}/bash-completion/completions/bspc
%{_datadir}/zsh/site-functions/_bspc
%{_datadir}/fish/vendor_completions.d/bspc.fish
%{_datadir}/xsessions/%{name}.desktop


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 5 2019 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.9-1
- Update to 0.9.9

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.2-1
- Update to 0.9.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9.1-1
- Update to 0.9.1
- Fix compliance to freedesktop specifications

* Sat Mar 12 2016 Oles Pidgornyy <pidgornyy@informatik.uni-frankfurt.de> - 0.9-1
- Initial release
