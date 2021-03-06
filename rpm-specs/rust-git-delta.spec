# Generated by rust2rpm 15
%bcond_without check
%global __cargo_skip_build 0

%global crate git-delta

Name:           rust-%{crate}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Syntax-highlighting pager for git

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/git-delta
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Syntax-highlighting pager for git.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# ASL 2.0
# ASL 2.0 or Boost
# BSD
# ISC
# LGPLv3+
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
# zlib
License:        MIT and ASL 2.0 and BSD and ISC and LGPLv3+ and zlib

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/delta
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/delta.bash
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_delta

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 etc/completion/completion.bash \
  -T %{buildroot}%{_datadir}/bash-completion/completions/delta.bash
install -Dpm0644 etc/completion/completion.zsh \
  -T %{buildroot}%{_datadir}/zsh/site-functions/_delta

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Aug 27 16:43:44 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sun Aug 16 15:01:28 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.1-4
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 08:01:45 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Update shell-words to 1

* Sat May 02 10:50:26 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
