Name:       imgp
Version:    2.7
Release:    3%{?dist}
Summary:    Multi-core batch image resizer and rotator

License:    GPLv3+
URL:        https://github.com/jarun/imgp
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make

Requires:   python3-pillow


%description
imgp is a command line image resizer and rotator for JPEG and PNG images. 
It can resize (or thumbnail) and rotate thousands of images in a go,
at lightning speed, while saving significantly on storage.

Powered by multiprocessing, an intelligent adaptive algorithm, 
recursive operations, shell completion scripts, EXIF preservation (and more), 
imgp is a very flexible utility with well-documented easy to use options.

imgp intends to be a stronger replacement of the Nautilus Image Converter 
extension, not tied to any file manager and way faster. On desktop environments 
(like Xfce or LxQt) which do not integrate Nautilus, imgp will save your day.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' imgp


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/imgp-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/imgp.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_imgp


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/imgp-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/imgp.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_imgp


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 23:45:22 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.7-1
- Release 2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.6-1
- Release 2.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.5-1
- First RPM release
