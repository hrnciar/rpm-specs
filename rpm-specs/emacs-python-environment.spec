%global pkg python-environment

Name:           emacs-%{pkg}
Version:        0.0.2
Release:        1%{?dist}
Summary:        Python virtualenv API for Emacs Lisp

License:        GPLv3+
URL:            https://github.com/tkf/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
BuildRequires:  emacs-deferred
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-deferred
Requires:       virtualenv
BuildArch:      noarch

%description
Emacs integrates well with external tools written in languages other than Emacs
Lisp and thus use of these tools should be encouraged. However, many people try
to avoid using non-Emacs Lisp software tools since it makes installation of
their Emacs plugin hard. python-environment.el solves this problem (only for the
case the tool is written in Python) by providing virtualenv API in Emacs Lisp so
that you can automate installation of tools written in Python.


%prep
%autosetup


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%files
%doc README.rst
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.2-1
- Initial RPM release
