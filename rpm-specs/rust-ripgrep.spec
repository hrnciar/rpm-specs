# Generated by rust2rpm 15
%bcond_without check
%global __cargo_skip_build 0

%global crate ripgrep

Name:           rust-%{crate}
Version:        12.1.1
Release:        1%{?dist}
Summary:        Line oriented search tool using Rust's regex library

# Upstream license specification: Unlicense OR MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/ripgrep
Source:         %{crates_source}
# Initial patched metadata
# * No simd
# * No jemalloc
Patch0:         ripgrep-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Line-oriented search tool that recursively searches your current directory for
a regex pattern while respecting your gitignore rules. ripgrep has first class
support on Windows, macOS and Linux.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# * ASL 2.0 or Boost
# * ASL 2.0 or MIT
# * MIT
# * MIT or ASL 2.0
# * Unlicense or MIT
License:        MIT and (Boost or ASL 2.0)

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-MIT UNLICENSE COPYING
%doc README.md CHANGELOG.md
%{_bindir}/rg
%{_mandir}/man1/rg.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/rg.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/rg.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_rg

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a
echo '/usr/bin/asciidoctor'

%build
%cargo_build -a

%install
%cargo_install -a
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  target/release/build/%{crate}-*/out/rg.1
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  target/release/build/%{crate}-*/out/rg.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  target/release/build/%{crate}-*/out/rg.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  complete/_rg

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
* Fri May 29 18:35:53 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 12.1.1-1
- Update to 12.1.1

* Sun May 10 10:02:13 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 12.1.0-1
- Update to 12.1.0

* Mon Mar 30 10:16:26 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 12.0.1-1
- Update to 12.0.1

* Tue Mar 17 16:49:50 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 12.0.0-1
- Update to 12.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 14:42:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.2-1
- Update to 11.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 18:29:00 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.1-4
- Correct fish completions directory

* Thu Jun 27 08:59:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.1-3
- Regenerate

* Sun Jun 09 12:38:07 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.1-2
- Regenerate

* Wed Apr 17 07:15:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.1-1
- Update to 11.0.1

* Tue Apr 16 13:45:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 11.0.0-1
- Update to 11.0.0

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-4
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-3
- Infra can't run tests

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-2
- Run tests in infrastructure

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Sat Aug 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.8.1-10
- Rebuild with fixed binutils

* Sun Jul 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-9
- Run real tests

* Sun Jul 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-8
- Bump encoding_rs to 0.8

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-7
- Bump termcolor to 1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-5
- Bump regex to 1

* Wed Apr 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org - 0.8.1-4
- Bump globset to 0.4

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 0.8.1-3
- Rebuild with new regex crates

* Fri Feb 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-2
- Restore spec

* Fri Feb 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Mon Feb 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-9
- Rebuild for bytecount 0.3.0

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-8
- Rebuild for rust-packaging v5

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-7
- Bump lazy_static to 1

* Tue Nov 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-6
- Rebuild for clap 2.28.0

* Thu Nov 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-5
- Fix bash completion

* Thu Nov 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-4
- Package completions

* Wed Nov 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-3
- Rebuild for dependency change

* Tue Nov 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-2
- Rebuild for dependency change

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Wed Jul 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-3
- Rebuild for clap

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-2
- Bump encoding_rs to 0.6

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Port to use rust-packaging

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-6
- Rename with rust prefix

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-5
- Rebuild

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-4
- Ship manpage

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-3
- Rebuild (termcolor)

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Rebuild (memmap)

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package