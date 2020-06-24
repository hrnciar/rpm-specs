%global pkg blacken

%global commit 1874018ae242176d0780cdcd0109e8f9a123a914
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20190521

Name:           emacs-%{pkg}
Version:        0
Release:        0.2.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Python Black for Emacs

License:        GPLv3+
URL:            https://github.com/proofit404/%{pkg}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       python3-black
BuildArch:      noarch

%description
Blacken uses black to format a Python buffer. It can be called explicitly on a
certain buffer, but more conveniently, a minor-mode 'blacken-mode' is provided
that turns on automatically running black on a buffer before saving.

To automatically format all Python buffers before saving, add the function
blacken-mode to python-mode-hook:

  (add-hook 'python-mode-hook 'blacken-mode)


%prep
%autosetup -n %{pkg}-%{commit}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190521git1874018
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.1.20190521git1874018
- Initial RPM release
