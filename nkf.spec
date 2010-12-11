%define	name         nkf
%define	version      2.07
%define	src_version  207b1
%define	release      %mkrel 0.3

Summary:   Network Kanji code conversion Filter
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   BSD-like
Group:     System/Internationalization
URL:       http://sourceforge.jp/projects/nkf/
Source:    http://prdownloads.sourceforge.jp/nkf/20055/%{name}%{src_version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Nkf is a yet another kanji code converter among networks, hosts and
terminals.  It converts input kanji code to designated kanji code such
as 7-bit JIS, MS-kanji (shifted-JIS) or EUC.

%prep
%setup -q -n %{name}207

%build
%make

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 nkf $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 nkf.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -m 644 nkf.1j $RPM_BUILD_ROOT%{_mandir}/ja/man1/nkf.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc nkf.doc
%{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja/man1/nkf.1*

