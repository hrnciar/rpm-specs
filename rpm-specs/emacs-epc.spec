%global pkg epc

Name:           emacs-%{pkg}
Version:        0.1.1
Release:        1%{?dist}
Summary:        A RPC stack for Emacs Lisp

License:        GPLv3+
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
BuildRequires:  emacs-ctable
BuildRequires:  emacs-deferred
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-ctable
Requires:       emacs-deferred
BuildArch:      noarch

%description
This program is an asynchronous RPC stack for Emacs. Using this RPC stack, the
Emacs can communicate with the peer process smoothly. Because the protocol
employs S-expression encoding and consists of asynchronous communications, the
RPC response is fairly good.


%prep
%autosetup


%build
for i in %{pkg}s.el %{pkg}.el; do
    %{_emacs_bytecompile} $i
done


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}s.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc readme.md
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.1-1
- Initial RPM release
