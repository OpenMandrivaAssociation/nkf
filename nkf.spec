Summary:	Network Kanji code conversion Filter
Name:		nkf
Version:	2.1.3
Release:	2
License:	BSD
Group:		System/Internationalization
Url:		http://sourceforge.jp/projects/nkf/
Source0:	http://prdownloads.sourceforge.jp/nkf/20055/%{name}-%{version}.tar.gz

%description
Nkf is a yet another kanji code converter among networks, hosts and
terminals.  It converts input kanji code to designated kanji code such
as 7-bit JIS, MS-kanji (shifted-JIS) or EUC.

%files
%doc nkf.doc
%{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja/man1/nkf.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" nkf

%install
install -d %{buildroot}%{_bindir}
install -m 755 nkf %{buildroot}%{_bindir}

install -d %{buildroot}%{_mandir}/man1
install -m 644 nkf.1 %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_mandir}/ja/man1
install -m 644 nkf.1j %{buildroot}%{_mandir}/ja/man1/nkf.1


